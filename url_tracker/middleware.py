from django import http
from django.conf import settings

from url_tracker.models import URLChangeRecord


class URLChangePermanentRedirectMiddleware(object):

    def process_response(self, request, response):
        if response.status_code != 404:
            return response # No need to check for non-404 responses.
        try:
            requested_url = request.path_info
            redirect_url = URLChangeRecord.objects.get(old_url__exact=requested_url)
            if redirect_url.deleted:
                return http.HttpResponseGone()
            else:
                return http.HttpResponsePermanentRedirect(redirect_url.new_url)
        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except (http.Http404, URLChangeRecord.DoesNotExist):
            return response
        except:
            if settings.DEBUG:
                raise
            return response
