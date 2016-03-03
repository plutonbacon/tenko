# Tenko Server API

The Tenko Server API is organized around [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer). It has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors. It also uses built-in HTTP features, like HTTP authentication and HTTP verbs, which are understood by off-the-shelf HTTP clients. JSON is returned by all API responses, including errors.

## Authentication

Authentication to the API is performed via [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Provide the API key as the basic auth username value. A password does not to be provided.

All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTP_Secure). Calls made over plain HTTP will fail. API requests without authentication will also fail.

**Example Request**

```
$ curl https://tenko.example.com/api/v1/sensors \
    -u ZcdTuyXi3piqHlHCFuRGRNcFUuTnrny:
```

cURL uses the -u flag to pass basic auth credentials (adding a colon after your API key prevents cURL from asking for a password).

## Errors

The Tenko Server API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the ```2xx``` range indicate success, codes in the ```4xx``` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, sensor creation failed, etc.), and codes in the ```5xx``` range indicate an error with the Tenko Server.

### Attributes

**type**
The type of error returned. Can be: ```authentication_error```, ```invalid_request_error```, etc._

**message** (optional)
A human-readable message providing more details about the error.

**param** (optional)
The parameter the error relates to if the error is parameter-specific.

### HTTP status code summary

**200 - OK**
Everything worked as expected.

**400 - Bad Request**
The request was unacceptable, often due to missing required parameter.

**401 - Unauthorized**
No valid API key provided.

**402 - Request Failed**
The parameters were valid but the request failed.

**404 - Not Found**
The requested resource does not exist.

**500,502,503,504 - Server Errors**
Something went wrong on the Tenko Server end.

### Errors - Types

**authentication_error**
Failure to properly authenticate yourself in a request.

**invalid_request_error**
Invalid request errors arise when your request has invalid parameters.