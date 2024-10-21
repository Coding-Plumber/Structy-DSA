# semesters required
# Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a single semester, as long as the prerequisites of a course are satisfied before taking it.
#
# Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.
#
# You can assume that it is possible to eventually complete all courses.


# Approach - build adjacency list, iterate through each index passing to a helper function, DFS as far out for all neighbors then return and keep track of each value to compare against and return longest semester.


num_courses = 6
prereqs = [
    (1, 2),
    (2, 4),
    (3, 5),
    (0, 5),
]
# semesters_required(num_courses, prereqs) # -> 3


def semesters_required(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)
    distance = {}

    for course in graph:
        if len(graph[course]) == 0:
            distance[course] = 1
    print(graph)
    for course in graph:
        traverse_distance(graph, course, distance)

    return max(distance.values())


def traverse_distance(graph, node, distance):
    if node in distance:
        return distance[node]

    longest_semester = 0

    for neighbor in graph[node]:
        count = traverse_distance(graph, neighbor, distance)
        longest_semester = max(count, longest_semester)

    distance[node] = 1 + longest_semester
    return distance[node]


def build_graph(num_courses, prereqs):
    graph = {}

    for course in range(num_courses):
        graph[course] = []

    for prereq in prereqs:
        a, b = prereq  # 1, 2
        graph[a].append(b)

    return graph


# p = # prereqs
# c = # courses
# Time: O(p)
# Space: O(c)
