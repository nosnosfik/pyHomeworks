def swap_quotes(some_string: str) -> str:
    quote_code = ord("'")
    dbl_quote_code = ord('"')
    my_dict = {quote_code: dbl_quote_code,
               dbl_quote_code: quote_code}
    return some_string.translate(my_dict)
