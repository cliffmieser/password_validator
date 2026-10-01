# Functions to test length, charset, and patterns 
import math
import string

def rate_length(pw: str) -> str:
    """Takes a password (pw) string and returns a string based on how weak or strong it is"""
    pw_len = len(pw)

    match (pw_len):
        case n if n < 8:
            return "weak"
        case n if 8 <= n  <= 12:
            return "moderate"
        case _:
            return "strong"


def rate_div(pw: str) -> dict:
    """ Takes a password and  calculates character pool size (R) for entropy calculation"""
    has_lower = any(c in string.ascii_lowercase for c in pw)
    has_upper = any(c in string.ascii_uppercase for c in pw)
    has_digit = any(c in string.digits for c in pw)
    has_symbol = any(c in string.punctuation for c in pw)

    pool_size = 0
    if has_lower:
        pool_size += 26 
    if has_upper:
        pool_size += 26 
    if has_digit:
        pool_size += 10 
    if has_symbol: 
        pool_size += len(string.punctuation) # 32 standard symbols 

    return {
        "length": len(pw),
        "has_lower": has_lower, 
        "has_upper": has_upper,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "pool_size": pool_size,
    }


def calc_entropy(pw_len: int, R: int | float) ->int:
    """computes password entropy in bits"""
    if R <= 0 or pw_len <= 0:
        return 0.0
    return float(pw_len) * math.log2(R)
    
            

