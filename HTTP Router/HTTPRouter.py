# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()


    def insert(self, path):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        list_of_path = split_path(path)
        current = self.root

        for l in list_of_path:
            if l not in current.children:
                current.insert(l)
        current = current.children[l]


    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        list_of_path = split_path(path)
        current = self.root

        for l in list_of_path:
            if l not in current.children:
                return None

            current = current.children[l]

        return current.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = {}


    def insert(self, l):
        # Insert the node as before
        self.children[l] = RouteTrieNode()

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, invalid_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrieNode()
        self.root_handler = root_handler
        self.invalid_handler = invalid_handler


    def add_handler(self, path, data):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        list_of_path = self.split_path(path)
        current = self.root

        for l in list_of_path:
            if l not in current.children:
                current.insert(l)

            current = current.children[l]
        current.handler = data


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == "/":
            return "root_handler"

        list_of_path = self.split_path(path)
        current = self.root

        for l in list_of_path:

            try:
                if current.children[l]:
                    current = current.children[l]

            except:
                return "invalid"

        if not current.handler:
            return "invalid"
        return current.handler


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path[0] == "/":
            path = path[1:]

        if path[-1] == "/":
            path = path[:-1]

        list_of_path = path.split("/")
        return list_of_path

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one