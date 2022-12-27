def one_replace_distance(firstStr, secondStr):
	if len(firstStr) != len(secondStr):
		return False
	differInOne = False
	for frstChar, secChar in zip(firstStr, secondStr):
		if frstChar != secChar:
			if differInOne:
				return False
			differInOne = True
	return differInOne

def one_more_less(firstStr, secondStr):
	if abs(len(firstStr) - len(secondStr)) != 1:
		return False
	shorter, longer = firstStr, secondStr
	if len(firstStr) > len(secondStr):
		shorter, longer = secondStr, firstStr

	firstPart, secondPart = longer, ""
	while firstPart != "":
		lastEl = firstPart[-1]
		if firstPart[:-1] + secondPart == shorter:
			return True
		firstPart = firstPart[:-1]
		secondPart = lastEl + secondPart
	return False


def is_one_edit_distance(firstStr, secondStr):
	if firstStr == secondStr:
		return False
	return one_replace_distance(firstStr, secondStr) or one_more_less(firstStr, secondStr)
