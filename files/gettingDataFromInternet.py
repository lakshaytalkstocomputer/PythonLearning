import http.client
import contextlib
import pprint

path_list = [
    "/wikipedia/commons/7/72/IPhone_Internals.jpg",
    "/wikipedia/en/c/c1/1drachmi_1973.jpg",
    "/wikipedia/commons/thumb/7/72/IPhone_Internals.jpg/800px-IPhone_Internals.jpg"
]

host = "upload.wikimedia.org"

with contextlib.closing(http.client.HTTPSConnection(host)) as connection:
    for path in path_list:
        connection.request("GET", path)
        response = connection.getresponse()
        print("Status : ", response.status)
        print("Headers: ", end="")
        pprint.pprint(response.getheaders())
        _, _, filename = path.rpartition("/")
        print("Writing: ", filename)
        with open(filename, "wb") as image:
            image.write(response.read())

