######################################################################
# CSE 231 Project #5
# Algorithm
#   1. Ask the user for a filename
#   2. Read the file and create a network
#   3. Create a similarity matrix
#   4. Ask the user for a user id
#   5. Recommend a friend for the user
#   6. Ask the user if they want to continue
#   7. If yes, repeat steps 4-6
#   8. If no, end the program
######################################################################

def open_file():
    """ This function asks the user for a filename and opens the file, then returns the file. """
    filename = input("Enter a filename: ")
    while True:
        try:
            fp = open(filename, "r")
            return fp
        except FileNotFoundError:
            print("Error in filename.")
            filename = input("Enter a filename: ")


def read_file(fp):
    """ This function reads the file and creates a network. """
    n = int(fp.readline().strip())
    network = []
    for i in range(n):
        network.append([])
    for line in fp:
        line = line.strip()
        line = line.split(" ")
        u = int(line[0])
        v = int(line[1])
        network[u].append(v)
        network[v].append(u)
    return network


def num_in_common_between_lists(list1, list2):
    """ This function takes two lists and returns the number of elements that are in both lists. """
    count = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                count += 1
    return count


def calc_similarity_scores(network):
    """ This function takes a network and returns a similarity matrix."""
    similarity_matrix = []
    for i in range(len(network)):
        similarity_matrix.append([])
    for i in range(len(network)):
        for j in range(len(network)):
            similarity_matrix[i].append(num_in_common_between_lists(network[i], network[j]))
    return similarity_matrix


def recommend(user_id, network, similarity_matrix):
    """ This function takes a user id, a network, and a similarity matrix and returns a friend recommendation. """
    count = 0
    for i in range(len(similarity_matrix[user_id])):
        if similarity_matrix[user_id][i] > count and i != user_id and i not in network[user_id]:
            count = similarity_matrix[user_id][i]
            index = i
    return index


def main():
    print("Facebook friend recommendation.\n")
    fp = open_file()
    network = read_file(fp)
    similarity_matrix = calc_similarity_scores(network)
    while True:
        user_id = input("Enter an integer in the range 0 to {}: ".format(len(network) - 1))
        # Check if user_id is an int
        try:
            user_id = int(user_id)
        # If not, print error message and continue
        except ValueError:
            print("Error: input must be an int between 0 and {}".format(len(network) - 1))
            continue
        # If it is, check if it is in the range
        if len(network) <= user_id or user_id <= -1:
            # If not, print error message and continue
            print("Error: input must be an int between 0 and {}".format(len(network) - 1))
            continue
        else:
            # If it is, recommend a friend
            index = recommend(user_id, network, similarity_matrix)
            print("The suggested friend for {} is {}".format(user_id, index))
        answer = input("\nDo you want to continue (yes/no)? ")
        # If user enters "no", end the program
        if answer.lower() == "no":
            break
        else:
            continue


if __name__ == "__main__":
    main()

