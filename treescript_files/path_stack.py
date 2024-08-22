"""Path Stack Management."""


class PathStack:
    """A Stack of Directory names in a Path."""

    def __init__(self):
        # The Stack of Directories in the Path.
        self._stack = []

    def push(self, directory_name: str):
        """Push a directory to the Path Stack.

        Parameters:
        - directory_name (str): The name of the next directory in the Path Stack.
        """
        self._stack.append(directory_name)

    def join_stack(self) -> str:
        """
        Combines all elements in the Stack to form a parent directory.

        Returns:
        str representing the current directory.
        """
        if len(self._stack) == 0:
            return ""
        return f"{'/'.join(self._stack)}/"

    def reduce_depth(self, depth: int) -> bool:
        """
        Reduce the Depth of the Path Stack.

        Parameters:
        - depth (int): The depth to reduce the stack to.

        Returns:
        boolean : Whether the Reduction was successful, ie 0 or more Stack pops.
        """
        current_depth = self.get_depth()
        if current_depth < depth or depth < 0:
            return False
        if current_depth == depth:
            return True
        for _ in range(current_depth, depth, -1):
            self._stack.pop()
        return True

    def get_depth(self) -> int:
        """
        Obtain the current Depth of the Stack.
            The state where the current directory is the path, ie: './' has a depth of 0.

        Returns:
        int : The number of elements in the Path Stack.
        """
        return len(self._stack)
