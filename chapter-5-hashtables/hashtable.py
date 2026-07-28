# Chapter 5 - Hash Tables (Caching Example)

cache = {}

def get_page(url):
    if url in cache:
        print("Fetching from cache...")
        return cache[url]

    print("Fetching from server...")
    data = f"Contents of {url}"  # Simulated server response
    cache[url] = data
    return data


# Test
print(get_page("google.com"))
print(get_page("youtube.com"))
print(get_page("google.com"))   # Retrieved from cache