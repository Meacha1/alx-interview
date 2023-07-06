def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes
        and their corresponding keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes  # List to track the unlocked
    unlocked[0] = True  # The first box is initially unlocked
    keys = boxes[0]  # Start with the keys from the first box

    # Iterate through the keys until no more boxes can be unlocked
    while keys:
        key = keys.pop()
        if key < num_boxes and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    return all(unlocked)
