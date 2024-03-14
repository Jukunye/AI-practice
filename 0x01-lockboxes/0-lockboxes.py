def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    :param boxes: List of lists, each containing keys to other boxes.
    :return: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list):
        return False

    n = len(boxes)
    if n == 0:
        return False

    unlocked = set([0])
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
