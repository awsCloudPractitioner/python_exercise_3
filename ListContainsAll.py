

# Give two lists, python function to answer if all elements of one list are in the other
class ListComparision:

    def has_common_elements(self, parentlist, childlist):

        # check if parentlist contains all elements in childlist
        result = all(elem in parentlist for elem in childlist)
        return result


if __name__ == "__main__":

    # Two lists of string
    parentList = ['Hi', 'hello', 'from']
    childList = ['Hi', 'Hi']

    instance = ListComparision()

    result = instance.has_common_elements(parentList, childList)
    if result:
        print("Yes, all elements of one list are in the other")
    else:
        print("No, all elements of one list are not in the other")

