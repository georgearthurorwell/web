def app(env, start_response):
    body = '\n'.join(env.get('QUERY_STRING').split('&'))
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return body
