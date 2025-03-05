class Solution:
    def simplifyPath(self, path: str) -> str:
        arr, stack = path.split("/"), []
        for i in range(len(arr)):
            if arr[i] != "" and arr[i] != "." and arr[i] != "..":
                stack.append(arr[i])
            elif arr[i] == ".." and stack:
                stack.pop()
        
        return "/" + "/".join(stack)