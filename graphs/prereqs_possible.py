# prereqs possible

# Write a function, prereqs_possible, that takes in a number of courses (n) and prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. The function should return a boolean indicating whether or not it is possible to complete all courses.


# numCourses = 6
# prereqs = [
#   (0, 1),
#   (2, 3),
#   (0, 2),
#   (1, 3),
#   (4, 5),
# ]
# prereqs_possible(numCourses, prereqs) # -> True

# Approach - We need to check for cycle detection, if we come accross the same node whilst visiting we know we have a cycle


def prereqs_possible(num_courses, prereqs):
    visited = set()
    graph = build_graph(num_courses, prereqs)

    for node in graph:
        if check_cycle(graph, node, visited, set()):
            return False
    return True


def check_cycle(graph, node, visited, visiting):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if check_cycle(graph, neighbor, visited, visiting):
            return True

    visiting.remove(node)
    visited.add(node)

    return False


def build_graph(num_courses, prereqs):
    graph = {}

    for num in range(0, num_courses):
        graph[num] = []

    for prereq in prereqs:
        course_a, course_b = prereq
        graph[course_a].append(course_b)

    return graph


# n = courses
# p = prereqs
# Time: O(n + p)
# Space: O(n + p)
