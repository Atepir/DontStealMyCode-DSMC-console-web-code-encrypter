class TestClass():
    def __init__(self, test_initializer):
        print("[INFO] Function initilized successfully")
        self.test_initializer = test_initializer

    def say_hello(self):
        guy = input("[INPUT] What is your name ? \n")
        print(f"Hello { guy }")
