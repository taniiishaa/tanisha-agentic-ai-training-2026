import asyncio

class Solution:
    async  def isValid(self, s):
        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if ch == ")" and top != "(":
                    return False
                if ch == "]" and top != "[":
                    return False
                if ch == "}" and top != "{":
                    return False

            await asyncio.sleep(0)

        return len(stack) == 0


obj = Solution()
print(asyncio.run(obj.isValid("([])")))