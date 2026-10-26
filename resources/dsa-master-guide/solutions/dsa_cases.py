"""Test cases for every runnable example in the DSA guide. Generated once from the verified content.

CASES maps a solution file to (prelude name or None, [(call, expected)]).
Expected values are written as Python literals so tuples, sets and floats keep their real types."""

CASES = {
    'concepts/c10_1.py': (None, [
        ('(lambda s: [s.push(1), s.push(2), s.pop(), s.peek(), s.size()])(Stack())', [None, None, 2, 1, 1]),
    ]),
    'concepts/c10_2.py': (None, [
        ('(lambda q: [q.enqueue(1), q.enqueue(2), q.dequeue(), q.size])(CircularQueue(2))', [True, True, 1, 1]),
    ]),
    'concepts/c10_3.py': (None, [
        ('is_balanced("{[()]}")', True),
        ('is_balanced("(]")', False),
    ]),
    'concepts/c10_3_stage1.py': (None, [
        ('next_greater([4, 5, 2, 25])', [5, 25, 25, -1]),
    ]),
    'concepts/c10_3_stage2.py': (None, [
        ('next_greater([4, 5, 2, 25])', [5, 25, 25, -1]),
    ]),
    'concepts/c11_1.py': (None, [
        ('fib(10)', 55),
        ('sum_digits(493)', 16),
    ]),
    'concepts/c11_1_stage1.py': (None, [
        ('fib(20)', 6765),
    ]),
    'concepts/c11_1_stage2.py': (None, [
        ('fib(20)', 6765),
    ]),
    'concepts/c11_1_stage3.py': (None, [
        ('fib(20)', 6765),
    ]),
    'concepts/c11_2.py': (None, [
        ('subsets([1,2,3])', [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
    ]),
    'concepts/c11_2_stage1.py': (None, [
        ('len(subsets([1, 2, 3]))', 8),
    ]),
    'concepts/c11_2_stage2.py': (None, [
        ('len(subsets([1, 2, 3]))', 8),
    ]),
    'concepts/c11_2_stage3.py': (None, [
        ('len(subsets([1, 2, 3]))', 8),
    ]),
    'concepts/c11_3.py': (None, [
        ('n_queens(4)', 2),
        ('n_queens(5)', 10),
    ]),
    'concepts/c12_1.py': ('tree', [
        ('inorder(build_tree([4,2,6,1,3]), [])', [1, 2, 3, 4, 6]),
        ('preorder(build_tree([4,2,6,1,3]), [])', [4, 2, 1, 3, 6]),
        ('postorder(build_tree([4,2,6,1,3]), [])', [1, 3, 2, 6, 4]),
    ]),
    'concepts/c12_2.py': ('tree', [
        ('bst_search(build_tree([8,3,10,1,6,None,14]),7)', False),
        ('bst_search(bst_insert(build_tree([2,1,3]),5),5)', True),
    ]),
    'concepts/c12_2_stage1.py': ('tree', [
        ('is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7]))', True),
    ]),
    'concepts/c12_2_stage2.py': ('tree', [
        ('is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7]))', False),
    ]),
    'concepts/c12_3.py': ('tree', [
        ('height(build_tree([1,2,3,4]))', 3),
        ('count_nodes(build_tree([1,2,3,4]))', 4),
        ('is_balanced(build_tree([1,2,2,3,None,None,3,4,None,None,4]))', False),
        ('is_balanced(build_tree([1,2,3]))', True),
    ]),
    'concepts/c12_3_stage1.py': ('tree', [
        ('is_balanced(build_tree([3, 9, 20, None, None, 15, 7]))', True),
    ]),
    'concepts/c12_3_stage2.py': ('tree', [
        ('is_balanced(build_tree([3, 9, 20, None, None, 15, 7]))', True),
    ]),
    'concepts/c13_1.py': (None, [
        ('(lambda h: ([h.push(x) for x in (5,3,8,1)], [h.pop() for _ in range(4)])[1])(MinHeap())', [1, 3, 5, 8]),
    ]),
    'concepts/c13_2.py': (None, [
        ('kth_largest([3,2,3,1,2,4,5,5,6],4)', 4),
    ]),
    'concepts/c13_2_stage1.py': (None, [
        ('kth_largest([3, 2, 1, 5, 6, 4], 2)', 5),
    ]),
    'concepts/c13_2_stage2.py': (None, [
        ('kth_largest([3, 2, 1, 5, 6, 4], 2)', 5),
    ]),
    'concepts/c14_1.py': (None, [
        ('dict(build_graph(3,[(0,1),(1,2)]))', {0: [1], 1: [0, 2], 2: [1]}),
        ('build_matrix(2,[(0,1)])', [[0, 1], [1, 0]]),
    ]),
    'concepts/c14_2.py': (None, [
        ('dfs({0:[1,2],1:[3],2:[3],3:[]},0)', [0, 1, 3, 2]),
    ]),
    'concepts/c14_3.py': (None, [
        ('region_size(["110","010","001"],0,0)', 3),
        ('region_size(["110","010","001"],2,2)', 1),
    ]),
    'concepts/c14_4.py': (None, [
        ('topo_sort(2,[(0,1),(1,0)])', []),
        ('dijkstra({0:[(1,4),(2,1)],1:[],2:[(1,2)]},0)', {0: 0, 2: 1, 1: 3}),
    ]),
    'concepts/c15_1.py': (None, [
        ('greedy_coins([1,3,4],6)', 3),
        ('dp_coins([1,3,4],6)', 2),
        ('greedy_coins([1,5,10,25],41)', 4),
    ]),
    'concepts/c15_1_stage1.py': (None, [
        ('coins([1, 3, 4], 6)', 3),
    ]),
    'concepts/c15_1_stage2.py': (None, [
        ('coins([1, 3, 4], 6)', 2),
    ]),
    'concepts/c15_2.py': (None, [
        ('select_activities([1,3,0,5,8,5],[2,4,6,7,9,9])', [(1, 2), (3, 4), (5, 7), (8, 9)]),
    ]),
    'concepts/c16_1.py': (None, [
        ('fib_tab(10)', 55),
        ('fib_memo(30)', 832040),
    ]),
    'concepts/c16_1_stage1.py': (None, [
        ('climb(10)', 89),
    ]),
    'concepts/c16_1_stage2.py': (None, [
        ('climb(10)', 89),
    ]),
    'concepts/c16_1_stage3.py': (None, [
        ('climb(10)', 89),
    ]),
    'concepts/c16_1_stage4.py': (None, [
        ('climb(10)', 89),
    ]),
    'concepts/c16_2.py': (None, [
        ('house_robber([2,7,9,3,1])', 12),
        ('coin_change([1,2,5],11)', 3),
    ]),
    'concepts/c16_2_stage1.py': (None, [
        ('rob([2, 7, 9, 3, 1])', 12),
    ]),
    'concepts/c16_2_stage2.py': (None, [
        ('rob([2, 7, 9, 3, 1])', 12),
    ]),
    'concepts/c16_2_stage3.py': (None, [
        ('rob([2, 7, 9, 3, 1])', 12),
    ]),
    'concepts/c16_3.py': (None, [
        ('lcs("abcde","ace")', 3),
        ('knapsack([1,3,4,5],[1,4,5,7],7)', 9),
    ]),
    'concepts/c16_3_stage1.py': (None, [
        ("lcs('abcde', 'ace')", 3),
    ]),
    'concepts/c16_3_stage2.py': (None, [
        ("lcs('abcde', 'ace')", 3),
    ]),
    'concepts/c16_3_stage3.py': (None, [
        ("lcs('abcde', 'ace')", 3),
    ]),
    'concepts/c17_1.py': (None, [
        ('get_bit(5,2)', 1),
        ('set_bit(4,0)', 5),
        ('clear_bit(7,1)', 5),
        ('toggle_bit(6,1)', 4),
        ('is_power_of_two(64)', True),
    ]),
    'concepts/c17_1_stage1.py': (None, [
        ('count_bits(11)', 3),
    ]),
    'concepts/c17_1_stage2.py': (None, [
        ('count_bits(11)', 3),
    ]),
    'concepts/c17_1_stage3.py': (None, [
        ('count_bits(11)', 3),
    ]),
    'concepts/c17_2.py': (None, [
        ('gcd(48,18)', 6),
        ('lcm(4,6)', 12),
        ('sieve(20)', [2, 3, 5, 7, 11, 13, 17, 19]),
        ('prime_factors(360)', [2, 2, 2, 3, 3, 5]),
    ]),
    'concepts/c17_2_stage1.py': (None, [
        ('count_primes(30)', 10),
    ]),
    'concepts/c17_2_stage2.py': (None, [
        ('count_primes(30)', 10),
    ]),
    'concepts/c17_2_stage3.py': (None, [
        ('count_primes(30)', 10),
    ]),
    'concepts/c17_3.py': (None, [
        ('mod_factorial(5)', 120),
        ('nCr(5,2)', 10),
        ('nCr(52,5)', 2598960),
    ]),
    'concepts/c18_1.py': (None, [
        ('(lambda t: [t.insert("to"), t.insert("tea"), t.search("to"), t.search("te"), t.starts_with("te")])(Trie())', [None, None, True, False, True]),
    ]),
    'concepts/c18_2.py': (None, [
        ('(lambda d: [d.union(0,1), d.union(1,2), d.union(0,2), d.groups])(DSU(4))', [True, True, False, 2]),
    ]),
    'concepts/c18_2_stage1.py': (None, [
        ('(lambda d: [d.union(0, 1), d.union(1, 2), d.union(0, 2)])(DSU(3))', [True, True, False]),
    ]),
    'concepts/c18_2_stage2.py': (None, [
        ('(lambda d: [d.union(0, 1), d.union(1, 2), d.union(0, 2)])(DSU(3))', [True, True, False]),
    ]),
    'concepts/c18_3.py': (None, [
        ('merge_intervals([[1,4],[0,4]])', [[0, 4]]),
    ]),
    'concepts/c18_4.py': (None, [
        ('transpose([[1,2],[3,4]])', [[1, 3], [2, 4]]),
        ('rotate_clockwise([[1,2],[3,4]])', [[3, 1], [4, 2]]),
        ('search_sorted_matrix([[1,4],[2,5]],5)', True),
    ]),
    'concepts/c18_5.py': (None, [
        ('rect_sum(build_2d_prefix([[1,2],[3,4]]),0,0,1,1)', 10),
        ('rect_sum(build_2d_prefix([[1,2],[3,4]]),1,0,1,1)', 7),
    ]),
    'concepts/c18_6.py': (None, [
        ('build_lps("ababaca")', [0, 0, 1, 2, 3, 0, 1]),
        ('build_lps("aabaa")', [0, 1, 0, 1, 2]),
    ]),
    'concepts/c18_7.py': (None, [
        ('(lambda f: ([f.update(i, v) for i, v in enumerate([3,2,1,4], 1)], f.range_sum(2,4))[1])(Fenwick(4))', 7),
    ]),
    'concepts/c1_1.py': (None, [
        ('summarize("3 5 8 10")', (18, 4, 10)),
    ]),
    'concepts/c1_1_stage1.py': (None, [
        ('digit_sum(493)', 16),
    ]),
    'concepts/c1_1_stage2.py': (None, [
        ('digit_sum(493)', 16),
    ]),
    'concepts/c1_2.py': (None, [
        ('count_divisible([4,7,8,9,12],4)', 3),
    ]),
    'concepts/c1_3.py': (None, [
        ('factorial(5)', 120),
    ]),
    'concepts/c2_1.py': (None, [
        ('ops_quadratic(10)', 100),
        ('ops_log(1024)', 10),
        ('ops_linear(7)', 7),
    ]),
    'concepts/c2_2.py': (None, [
        ('has_duplicate_slow([1,2,1])', True),
        ('has_duplicate_fast([1,2,3])', False),
    ]),
    'concepts/c2_2_stage1.py': (None, [
        ('has_duplicate([3, 1, 4, 1])', True),
    ]),
    'concepts/c2_2_stage2.py': (None, [
        ('has_duplicate([3, 1, 4, 1])', True),
    ]),
    'concepts/c2_2_stage3.py': (None, [
        ('has_duplicate([3, 1, 4, 1])', True),
    ]),
    'concepts/c3_1.py': (None, [
        ('reverse_in_place([1,2,3])', [3, 2, 1]),
    ]),
    'concepts/c3_2.py': (None, [
        ('find_duplicates([4,1,4,2,1])', [4, 1]),
    ]),
    'concepts/c3_2_stage1.py': (None, [
        ('missing_number([3, 0, 1])', 2),
    ]),
    'concepts/c3_2_stage2.py': (None, [
        ('missing_number([3, 0, 1])', 2),
    ]),
    'concepts/c3_2_stage3.py': (None, [
        ('missing_number([3, 0, 1])', 2),
    ]),
    'concepts/c3_2_stage4.py': (None, [
        ('missing_number([3, 0, 1])', 2),
    ]),
    'concepts/c3_3.py': (None, [
        ('kadane([-3,-1,-2])', -1),
        ('kadane([1,2,3])', 6),
    ]),
    'concepts/c3_3_stage1.py': (None, [
        ('max_subarray([-2, 1, -3, 4, -1, 2])', 5),
    ]),
    'concepts/c3_3_stage2.py': (None, [
        ('max_subarray([-2, 1, -3, 4, -1, 2])', 5),
    ]),
    'concepts/c3_3_stage3.py': (None, [
        ('max_subarray([-2, 1, -3, 4, -1, 2])', 5),
    ]),
    'concepts/c4_1.py': (None, [
        ('is_palindrome("abba")', True),
        ('is_palindrome("abc")', False),
    ]),
    'concepts/c4_1_stage1.py': (None, [
        ("is_palindrome('level')", True),
    ]),
    'concepts/c4_1_stage2.py': (None, [
        ("is_palindrome('level')", True),
    ]),
    'concepts/c4_2.py': (None, [
        ('is_anagram("rat","car")', False),
    ]),
    'concepts/c4_2_stage1.py': (None, [
        ("is_anagram('listen', 'silent')", True),
    ]),
    'concepts/c4_2_stage2.py': (None, [
        ("is_anagram('listen', 'silent')", True),
    ]),
    'concepts/c4_2_stage3.py': (None, [
        ("is_anagram('listen', 'silent')", True),
    ]),
    'concepts/c4_3.py': (None, [
        ('rabin_karp("abababa","aba")', [0, 2, 4]),
        ('rabin_karp("abc","d")', []),
    ]),
    'concepts/c5_1.py': (None, [
        ('binary_search([1,3,5],4)', -1),
    ]),
    'concepts/c5_1_stage1.py': (None, [
        ('search([1, 3, 5, 7, 9], 7)', 3),
    ]),
    'concepts/c5_1_stage2.py': (None, [
        ('search([1, 3, 5, 7, 9], 7)', 3),
    ]),
    'concepts/c5_1_stage3.py': (None, [
        ('search([1, 3, 5, 7, 9], 7)', 3),
    ]),
    'concepts/c5_2.py': (None, [
        ('lower_bound([1,3,5,6],2)', 1),
        ('lower_bound([1,3,5,6],7)', 4),
    ]),
    'concepts/c5_3.py': (None, [
        ('min_eating_speed([3,6,7,11],8)', 4),
        ('min_eating_speed([30,11,23,4,20],5)', 30),
        ('min_eating_speed([30,11,23,4,20],6)', 23),
    ]),
    'concepts/c6_1.py': (None, [
        ('insertion_sort([5,2,4,6,1,3])', [1, 2, 3, 4, 5, 6]),
    ]),
    'concepts/c6_1_stage1.py': (None, [
        ('sort([5, 2, 4, 1])', [1, 2, 4, 5]),
    ]),
    'concepts/c6_1_stage2.py': (None, [
        ('sort([5, 2, 4, 1])', [1, 2, 4, 5]),
    ]),
    'concepts/c6_1_stage3.py': (None, [
        ('sort([5, 2, 4, 1])', [1, 2, 4, 5]),
    ]),
    'concepts/c6_2.py': (None, [
        ('merge_sort([5,2,9,1,5,6])', [1, 2, 5, 5, 6, 9]),
        ('quick_sort([3,6,1,8,2,9,2])', [1, 2, 2, 3, 6, 8, 9]),
    ]),
    'concepts/c6_3.py': (None, [
        ('counting_sort([4,2,2,8,3,3,1])', [1, 2, 2, 3, 3, 4, 8]),
        ('heap_sort([9,4,7,1,5])', [1, 4, 5, 7, 9]),
    ]),
    'concepts/c7_1.py': (None, [
        ('simple_hash("cat")', 4),
    ]),
    'concepts/c7_2.py': (None, [
        ('pair_exists([3],6)', False),
        ('pair_exists([3,3],6)', True),
    ]),
    'concepts/c7_2_stage1.py': (None, [
        ('two_sum([2, 7, 11, 15], 9)', [0, 1]),
    ]),
    'concepts/c7_2_stage2.py': (None, [
        ('two_sum([2, 7, 11, 15], 9)', [0, 1]),
    ]),
    'concepts/c7_3.py': (None, [
        ('sorted(map(sorted, group_by_signature(["eat","tea","tan","ate"])))', [['ate', 'eat', 'tea'], ['tan']]),
    ]),
    'concepts/c7_3_stage1.py': (None, [
        ('longest([100, 4, 200, 1, 3, 2])', 4),
    ]),
    'concepts/c7_3_stage2.py': (None, [
        ('longest([100, 4, 200, 1, 3, 2])', 4),
    ]),
    'concepts/c8_1.py': (None, [
        ('is_pair_sum([1,2,3],7)', False),
    ]),
    'concepts/c8_1_stage1.py': (None, [
        ('has_pair([1, 3, 4, 6, 9], 10)', True),
    ]),
    'concepts/c8_1_stage2.py': (None, [
        ('has_pair([1, 3, 4, 6, 9], 10)', True),
    ]),
    'concepts/c8_1_stage3.py': (None, [
        ('has_pair([1, 3, 4, 6, 9], 10)', True),
    ]),
    'concepts/c8_2.py': (None, [
        ('max_window_sum([2,1,5,1,3,2],3)', 9),
    ]),
    'concepts/c8_2_stage1.py': (None, [
        ('best_window([2, 1, 5, 1, 3, 2], 3)', 9),
    ]),
    'concepts/c8_2_stage2.py': (None, [
        ('best_window([2, 1, 5, 1, 3, 2], 3)', 9),
    ]),
    'concepts/c8_3.py': (None, [
        ('longest_without_repeat("abba")', 2),
    ]),
    'concepts/c8_3_stage1.py': (None, [
        ("longest('abcabcbb')", 3),
    ]),
    'concepts/c8_3_stage2.py': (None, [
        ("longest('abcabcbb')", 3),
    ]),
    'concepts/c8_3_stage3.py': (None, [
        ("longest('abcabcbb')", 3),
    ]),
    'concepts/c9_1.py': ('ll', [
        ('to_list(delete_value(build([1,2,3]),1))', [2, 3]),
        ('to_list(delete_value(build([1,2,3]),9))', [1, 2, 3]),
    ]),
    'concepts/c9_2.py': ('ll', [
        ('to_list(reverse_list(build([1,2,3])))', [3, 2, 1]),
    ]),
    'concepts/c9_2_stage1.py': ('ll', [
        ('to_list(reverse_list(build([1, 2, 3])))', [3, 2, 1]),
    ]),
    'concepts/c9_2_stage2.py': ('ll', [
        ('to_list(reverse_list(build([1, 2, 3])))', [3, 2, 1]),
    ]),
    'concepts/c9_3.py': ('ll', [
        ('has_cycle(build([1,2,3]))', False),
    ]),
    'concepts/c9_3_stage1.py': ('ll', [
        ('has_cycle(build([3, 2, 0, -4], 1))', True),
    ]),
    'concepts/c9_3_stage2.py': ('ll', [
        ('has_cycle(build([3, 2, 0, -4], 1))', True),
    ]),
    'problems/add_binary.py': (None, [
        ('add_binary("11","1")', '100'),
        ('add_binary("1010","1011")', '10101'),
        ('add_binary("0","0")', '0'),
    ]),
    'problems/add_two_numbers.py': ('ll', [
        ('to_list(add_two_numbers(build([2,4,3]),build([5,6,4])))', [7, 0, 8]),
        ('to_list(add_two_numbers(build([9,9]),build([1])))', [0, 0, 1]),
        ('to_list(add_two_numbers(build([0]),build([0])))', [0]),
    ]),
    'problems/assign_cookies.py': (None, [
        ('assign_cookies([1,2,3],[1,1])', 1),
        ('assign_cookies([1,2],[1,2,3])', 2),
        ('assign_cookies([1],[])', 0),
    ]),
    'problems/asteroid_collision.py': (None, [
        ('asteroid_collision([5,10,-5])', [5, 10]),
        ('asteroid_collision([8,-8])', []),
        ('asteroid_collision([10,2,-5])', [10]),
        ('asteroid_collision([-2,-1,1,2])', [-2, -1, 1, 2]),
    ]),
    'problems/basic_calculator_ii.py': (None, [
        ('basic_calculator_ii("3+2*2")', 7),
        ('basic_calculator_ii(" 3/2 ")', 1),
        ('basic_calculator_ii(" 3+5 / 2 ")', 5),
        ('basic_calculator_ii("14-3/2")', 13),
    ]),
    'problems/best_time_stock_ii.py': (None, [
        ('best_time_stock_ii([7,1,5,3,6,4])', 7),
        ('best_time_stock_ii([1,2,3,4,5])', 4),
        ('best_time_stock_ii([7,6,4,3,1])', 0),
        ('best_time_stock_ii([5])', 0),
    ]),
    'problems/bfs_order.py': (None, [
        ('bfs_order({0:[1,2],1:[3],2:[3],3:[]},0)', [0, 1, 2, 3]),
        ('bfs_order({0:[]},0)', [0]),
        ('bfs_order({0:[1],1:[0]},0)', [0, 1]),
    ]),
    'problems/binary_search.py': (None, [
        ('binary_search([-1,0,3,5,9,12],9)', 4),
        ('binary_search([-1,0,3,5,9,12],2)', -1),
        ('binary_search([],1)', -1),
        ('binary_search([5],5)', 0),
        ('binary_search([1,2],2)', 1),
    ]),
    'problems/bubble_swaps.py': (None, [
        ('bubble_swaps([3,2,1])', 3),
        ('bubble_swaps([1,2,3])', 0),
        ('bubble_swaps([5,4,3,2,1])', 10),
        ('bubble_swaps([])', 0),
    ]),
    'problems/build_tree_pre_in.py': ('tree', [
        ('level_values(build_tree_pre_in([3,9,20,15,7],[9,3,15,20,7]))', [3, 9, 20, 15, 7]),
        ('level_values(build_tree_pre_in([1],[1]))', [1]),
        ('level_values(build_tree_pre_in([1,2],[2,1]))', [1, 2]),
    ]),
    'problems/burst_balloons.py': (None, [
        ('burst_balloons([3,1,5,8])', 167),
        ('burst_balloons([1,5])', 10),
        ('burst_balloons([7])', 7),
        ('burst_balloons([])', 0),
    ]),
    'problems/can_finish.py': (None, [
        ('can_finish(2,[[1,0]])', True),
        ('can_finish(2,[[1,0],[0,1]])', False),
        ('can_finish(3,[])', True),
        ('can_finish(1,[[0,0]])', False),
    ]),
    'problems/can_jump.py': (None, [
        ('can_jump([2,3,1,1,4])', True),
        ('can_jump([3,2,1,0,4])', False),
        ('can_jump([0])', True),
        ('can_jump([0,1])', False),
    ]),
    'problems/candy.py': (None, [
        ('candy([1,0,2])', 5),
        ('candy([1,2,2])', 4),
        ('candy([5])', 1),
        ('candy([1,2,3,4])', 10),
    ]),
    'problems/cheapest_flights.py': (None, [
        ('cheapest_flights(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1)', 200),
        ('cheapest_flights(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0)', 500),
        ('cheapest_flights(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1)', 700),
        ('cheapest_flights(2,[],0,1,3)', -1),
    ]),
    'problems/check_inclusion.py': (None, [
        ('check_inclusion("ab","eidbaooo")', True),
        ('check_inclusion("ab","eidboaoo")', False),
        ('check_inclusion("abc","ab")', False),
        ('check_inclusion("a","a")', True),
    ]),
    'problems/climb_stairs.py': (None, [
        ('climb_stairs(1)', 1),
        ('climb_stairs(2)', 2),
        ('climb_stairs(3)', 3),
        ('climb_stairs(5)', 8),
        ('climb_stairs(10)', 89),
    ]),
    'problems/coin_change.py': (None, [
        ('coin_change([1,2,5],11)', 3),
        ('coin_change([2],3)', -1),
        ('coin_change([1],0)', 0),
        ('coin_change([1,3,4],6)', 2),
    ]),
    'problems/coin_change_ii.py': (None, [
        ('coin_change_ii(5,[1,2,5])', 4),
        ('coin_change_ii(3,[2])', 0),
        ('coin_change_ii(10,[10])', 1),
        ('coin_change_ii(0,[7])', 1),
    ]),
    'problems/combination_sum.py': (None, [
        ('combination_sum([2,3,6,7],7)', [[2, 2, 3], [7]]),
        ('combination_sum([2,3,5],8)', [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ('combination_sum([2],1)', []),
    ]),
    'problems/combination_sum_ii.py': (None, [
        ('combination_sum_ii([10,1,2,7,6,1,5],8)', [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ('combination_sum_ii([2,5,2,1,2],5)', [[1, 2, 2], [5]]),
        ('combination_sum_ii([2],1)', []),
    ]),
    'problems/compress_string.py': (None, [
        ('compress_string("aaabbc")', 'a3b2c1'),
        ('compress_string("")', ''),
        ('compress_string("abc")', 'a1b1c1'),
        ('compress_string("zzzz")', 'z4'),
    ]),
    'problems/contains_duplicate.py': (None, [
        ('contains_duplicate([1,2,3,1])', True),
        ('contains_duplicate([1,2,3])', False),
        ('contains_duplicate([])', False),
    ]),
    'problems/count_bits_list.py': (None, [
        ('count_bits_list(5)', [0, 1, 1, 2, 1, 2]),
        ('count_bits_list(0)', [0]),
        ('count_bits_list(8)[-1]', 1),
    ]),
    'problems/count_components.py': (None, [
        ('count_components(5,[[0,1],[1,2],[3,4]])', 2),
        ('count_components(4,[])', 4),
        ('count_components(0,[])', 0),
        ('count_components(3,[[0,1],[1,2],[2,0]])', 1),
    ]),
    'problems/count_divisors.py': (None, [
        ('count_divisors(36)', 9),
        ('count_divisors(1)', 1),
        ('count_divisors(13)', 2),
        ('count_divisors(100)', 9),
    ]),
    'problems/count_inversions.py': (None, [
        ('count_inversions([2,4,1,3,5])', 3),
        ('count_inversions([5,4,3,2,1])', 10),
        ('count_inversions([1,2,3])', 0),
        ('count_inversions([2,2,2])', 0),
    ]),
    'problems/count_primes.py': (None, [
        ('count_primes(10)', 4),
        ('count_primes(2)', 0),
        ('count_primes(100)', 25),
        ('count_primes(3)', 1),
    ]),
    'problems/count_set_bits.py': (None, [
        ('count_set_bits(11)', 3),
        ('count_set_bits(0)', 0),
        ('count_set_bits(128)', 1),
        ('count_set_bits(255)', 8),
    ]),
    'problems/count_vowels.py': (None, [
        ('count_vowels("Infosys Limited")', 5),
        ('count_vowels("")', 0),
        ('count_vowels("rhythm")', 0),
        ('count_vowels("AEIOU")', 5),
    ]),
    'problems/course_order.py': (None, [
        ('(lambda o: sorted(o) == [0,1,2,3] and o.index(0) < o.index(1) and o.index(0) < o.index(2) and o.index(1) < o.index(3) and o.index(2) < o.index(3))(course_order(4,[[1,0],[2,0],[3,1],[3,2]]))', True),
        ('course_order(2,[[1,0],[0,1]])', []),
        ('sorted(course_order(3,[]))', [0, 1, 2]),
    ]),
    'problems/cycle_start.py': ('ll', [
        ('cycle_start(build([3,2,0,-4],1))', 2),
        ('cycle_start(build([1,2]))', None),
        ('cycle_start(build([1,2,3],0))', 1),
    ]),
    'problems/daily_temperatures.py': (None, [
        ('daily_temperatures([73,74,75,71,69,72,76,73])', [1, 1, 4, 2, 1, 1, 0, 0]),
        ('daily_temperatures([30,40,50,60])', [1, 1, 1, 0]),
        ('daily_temperatures([30])', [0]),
    ]),
    'problems/decode_string.py': (None, [
        ('decode_string("3[a2[c]]")', 'accaccacc'),
        ('decode_string("2[ab]c")', 'ababc'),
        ('decode_string("abc")', 'abc'),
        ('decode_string("10[a]")', 'aaaaaaaaaa'),
    ]),
    'problems/decode_ways.py': (None, [
        ('decode_ways("226")', 3),
        ('decode_ways("12")', 2),
        ('decode_ways("06")', 0),
        ('decode_ways("10")', 1),
        ('decode_ways("100")', 0),
    ]),
    'problems/delete_duplicates_list.py': ('ll', [
        ('to_list(delete_duplicates_list(build([1,1,2,3,3])))', [1, 2, 3]),
        ('to_list(delete_duplicates_list(build([])))', []),
        ('to_list(delete_duplicates_list(build([5,5,5])))', [5]),
    ]),
    'problems/diagonal_sum.py': (None, [
        ('diagonal_sum([[1,2,3],[4,5,6],[7,8,9]])', 25),
        ('diagonal_sum([[1,2],[3,4]])', 10),
        ('diagonal_sum([[5]])', 5),
    ]),
    'problems/diameter_tree.py': ('tree', [
        ('diameter_tree(build_tree([1,2,3,4,5]))', 3),
        ('diameter_tree(build_tree([1]))', 0),
        ('diameter_tree(build_tree([1,2]))', 1),
    ]),
    'problems/difference_array.py': (None, [
        ('difference_array(5,[[1,3,2],[2,4,3],[0,2,-2]])', [-2, 0, 3, 5, 3]),
        ('difference_array(3,[])', [0, 0, 0]),
        ('difference_array(1,[[0,0,5]])', [5]),
    ]),
    'problems/digit_sum.py': (None, [
        ('digit_sum(493)', 16),
        ('digit_sum(0)', 0),
        ('digit_sum(7)', 7),
        ('digit_sum(1000)', 1),
    ]),
    'problems/edit_distance.py': (None, [
        ('edit_distance("horse","ros")', 3),
        ('edit_distance("","abc")', 3),
        ('edit_distance("abc","abc")', 0),
        ('edit_distance("intention","execution")', 5),
    ]),
    'problems/equilibrium_index.py': (None, [
        ('equilibrium_index([1,7,3,6,5,6])', 3),
        ('equilibrium_index([1,2,3])', -1),
        ('equilibrium_index([2,1,-1])', 0),
        ('equilibrium_index([0])', 0),
    ]),
    'problems/eval_postfix.py': (None, [
        ('eval_postfix(["2","1","+","3","*"])', 9),
        ('eval_postfix(["4","13","5","/","+"])', 6),
        ('eval_postfix(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])', 22),
        ('eval_postfix(["7"])', 7),
    ]),
    'problems/excel_column_number.py': (None, [
        ('excel_column_number("A")', 1),
        ('excel_column_number("AB")', 28),
        ('excel_column_number("ZY")', 701),
    ]),
    'problems/fast_power.py': (None, [
        ('fast_power(2,10)', 1024),
        ('fast_power(3,0)', 1),
        ('fast_power(2,30)', 1073741824),
        ('fast_power(5,3)', 125),
    ]),
    'problems/fib_list.py': (None, [
        ('fib_list(6)', [0, 1, 1, 2, 3, 5]),
        ('fib_list(0)', []),
        ('fib_list(1)', [0]),
        ('fib_list(10)[-1]', 34),
    ]),
    'problems/fib_memo.py': (None, [
        ('fib_memo(10)', 55),
        ('fib_memo(0)', 0),
        ('fib_memo(1)', 1),
        ('fib_memo(50)', 12586269025),
    ]),
    'problems/find_all.py': (None, [
        ('find_all("abababa","aba")', [0, 2, 4]),
        ('find_all("hello","ll")', [2]),
        ('find_all("aaa","b")', []),
        ('find_all("ab","abc")', []),
    ]),
    'problems/find_all_anagrams.py': (None, [
        ('find_all_anagrams("cbaebabacd","abc")', [0, 6]),
        ('find_all_anagrams("abab","ab")', [0, 1, 2]),
        ('find_all_anagrams("a","ab")', []),
    ]),
    'problems/find_duplicate_number.py': (None, [
        ('find_duplicate_number([1,3,4,2,2])', 2),
        ('find_duplicate_number([3,1,3,4,2])', 3),
        ('find_duplicate_number([1,1])', 1),
    ]),
    'problems/find_min_rotated.py': (None, [
        ('find_min_rotated([3,4,5,1,2])', 1),
        ('find_min_rotated([4,5,6,7,0,1,2])', 0),
        ('find_min_rotated([1])', 1),
        ('find_min_rotated([1,2,3])', 1),
    ]),
    'problems/find_peak.py': (None, [
        ('find_peak([1,2,3,1])', 2),
        ('find_peak([1])', 0),
        ('find_peak([1,2,3,4])', 3),
        ('find_peak([4,3,2,1])', 0),
    ]),
    'problems/first_last.py': (None, [
        ('first_last([5,7,7,8,8,10],8)', [3, 4]),
        ('first_last([5,7,7,8,8,10],6)', [-1, -1]),
        ('first_last([],0)', [-1, -1]),
        ('first_last([2,2,2],2)', [0, 2]),
    ]),
    'problems/first_repeating.py': (None, [
        ('first_repeating([10,5,3,4,3,5,6])', 5),
        ('first_repeating([1,2,3])', -1),
        ('first_repeating([2,2])', 2),
    ]),
    'problems/first_unique_char.py': (None, [
        ('first_unique_char("leetcode")', 0),
        ('first_unique_char("loveleetcode")', 2),
        ('first_unique_char("aabb")', -1),
        ('first_unique_char("z")', 0),
    ]),
    'problems/fizzbuzz.py': (None, [
        ('fizzbuzz(5)', ['1', '2', 'Fizz', '4', 'Buzz']),
        ('fizzbuzz(15)[-1]', 'FizzBuzz'),
        ('fizzbuzz(1)', ['1']),
    ]),
    'problems/flood_fill.py': (None, [
        ('flood_fill([[1,1,0],[1,0,0]],0,0,2)', [[2, 2, 0], [2, 0, 0]]),
        ('flood_fill([[0,0],[0,0]],0,0,0)', [[0, 0], [0, 0]]),
        ('flood_fill([[1]],0,0,5)', [[5]]),
    ]),
    'problems/four_sum_count.py': (None, [
        ('four_sum_count([1,2],[-2,-1],[-1,2],[0,2])', 2),
        ('four_sum_count([0],[0],[0],[0])', 1),
    ]),
    'problems/fractional_knapsack.py': (None, [
        ('fractional_knapsack([60,100,120],[10,20,30],50)', 240.0),
        ('fractional_knapsack([10],[5],0)', 0.0),
        ('fractional_knapsack([10],[5],100)', 10.0),
    ]),
    'problems/fruit_baskets.py': (None, [
        ('fruit_baskets([1,2,1])', 3),
        ('fruit_baskets([0,1,2,2])', 3),
        ('fruit_baskets([1,2,3,2,2])', 4),
        ('fruit_baskets([3,3,3,1,2,1,1,2,3,3,4])', 5),
    ]),
    'problems/game_of_life.py': (None, [
        ('game_of_life([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])', [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]),
        ('game_of_life([[1,1],[1,0]])', [[1, 1], [1, 1]]),
    ]),
    'problems/gas_station.py': (None, [
        ('gas_station([1,2,3,4,5],[3,4,5,1,2])', 3),
        ('gas_station([2,3,4],[3,4,3])', -1),
        ('gas_station([5],[4])', 0),
    ]),
    'problems/gcd_lcm.py': (None, [
        ('gcd_lcm(12,18)', (6, 36)),
        ('gcd_lcm(7,13)', (1, 91)),
        ('gcd_lcm(5,5)', (5, 5)),
        ('gcd_lcm(4,16)', (4, 16)),
    ]),
    'problems/gcd_of_strings.py': (None, [
        ('gcd_of_strings("ABCABC","ABC")', 'ABC'),
        ('gcd_of_strings("ABABAB","ABAB")', 'AB'),
        ('gcd_of_strings("LEET","CODE")', ''),
    ]),
    'problems/generate_parentheses.py': (None, [
        ('generate_parentheses(3)', ['((()))', '(()())', '(())()', '()(())', '()()()']),
        ('generate_parentheses(1)', ['()']),
        ('len(generate_parentheses(4))', 14),
    ]),
    'problems/good_nodes.py': ('tree', [
        ('good_nodes(build_tree([3,1,4,3,None,1,5]))', 4),
        ('good_nodes(build_tree([3,3,None,4,2]))', 3),
        ('good_nodes(build_tree([1]))', 1),
    ]),
    'problems/group_anagrams.py': (None, [
        ('group_anagrams(["eat","tea","tan","ate","nat","bat"])', [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]),
        ('group_anagrams([""])', [['']]),
        ('group_anagrams([])', []),
    ]),
    'problems/hamming_distance.py': (None, [
        ('hamming_distance(1,4)', 2),
        ('hamming_distance(3,1)', 1),
        ('hamming_distance(7,7)', 0),
        ('hamming_distance(0,255)', 8),
    ]),
    'problems/happy_number.py': (None, [
        ('happy_number(19)', True),
        ('happy_number(2)', False),
        ('happy_number(1)', True),
        ('happy_number(7)', True),
    ]),
    'problems/has_cycle.py': ('ll', [
        ('has_cycle(build([3,2,0,-4],1))', True),
        ('has_cycle(build([1,2]))', False),
        ('has_cycle(build([]))', False),
        ('has_cycle(build([1],0))', True),
    ]),
    'problems/has_cycle_undirected.py': (None, [
        ('has_cycle_undirected(3,[[0,1],[1,2],[2,0]])', True),
        ('has_cycle_undirected(3,[[0,1],[1,2]])', False),
        ('has_cycle_undirected(2,[[0,1],[0,1]])', True),
    ]),
    'problems/has_path_sum.py': ('tree', [
        ('has_path_sum(build_tree([5,4,8,11,None,13,4,7,2]),22)', True),
        ('has_path_sum(build_tree([1,2,3]),5)', False),
        ('has_path_sum(None,0)', False),
        ('has_path_sum(build_tree([1]),1)', True),
    ]),
    'problems/house_robber.py': (None, [
        ('house_robber([1,2,3,1])', 4),
        ('house_robber([2,7,9,3,1])', 12),
        ('house_robber([])', 0),
        ('house_robber([5])', 5),
        ('house_robber([2,1])', 2),
    ]),
    'problems/house_robber_ii.py': (None, [
        ('house_robber_ii([2,3,2])', 3),
        ('house_robber_ii([1,2,3,1])', 4),
        ('house_robber_ii([1])', 1),
        ('house_robber_ii([1,2])', 2),
    ]),
    'problems/inorder.py': ('tree', [
        ('inorder(build_tree([2,1,3]))', [1, 2, 3]),
        ('inorder(build_tree([1,None,2,3]))', [1, 3, 2]),
        ('inorder(None)', []),
    ]),
    'problems/insert_interval.py': (None, [
        ('insert_interval([[1,3],[6,9]],[2,5])', [[1, 5], [6, 9]]),
        ('insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])', [[1, 2], [3, 10], [12, 16]]),
        ('insert_interval([],[5,7])', [[5, 7]]),
    ]),
    'problems/insertion_sort_impl.py': (None, [
        ('insertion_sort_impl([5,2,4,1])', [1, 2, 4, 5]),
        ('insertion_sort_impl([])', []),
        ('insertion_sort_impl([2,2,1])', [1, 2, 2]),
    ]),
    'problems/int_to_roman.py': (None, [
        ('int_to_roman(58)', 'LVIII'),
        ('int_to_roman(1994)', 'MCMXCIV'),
        ('int_to_roman(4)', 'IV'),
        ('int_to_roman(3999)', 'MMMCMXCIX'),
    ]),
    'problems/intersection.py': (None, [
        ('intersection([1,2,2,1],[2,2])', [2]),
        ('intersection([4,9,5],[9,4,9,8,4])', [4, 9]),
        ('intersection([1],[2])', []),
    ]),
    'problems/invert_tree.py': ('tree', [
        ('level_values(invert_tree(build_tree([4,2,7,1,3,6,9])))', [4, 7, 2, 9, 6, 3, 1]),
        ('level_values(invert_tree(None))', []),
        ('level_values(invert_tree(build_tree([1,2])))', [1, 2]),
    ]),
    'problems/is_anagram.py': (None, [
        ('is_anagram("listen","silent")', True),
        ('is_anagram("rat","car")', False),
        ('is_anagram("aab","abb")', False),
        ('is_anagram("","")', True),
    ]),
    'problems/is_armstrong.py': (None, [
        ('is_armstrong(153)', True),
        ('is_armstrong(9474)', True),
        ('is_armstrong(10)', False),
        ('is_armstrong(0)', True),
    ]),
    'problems/is_bipartite.py': (None, [
        ('is_bipartite([[1,3],[0,2],[1,3],[0,2]])', True),
        ('is_bipartite([[1,2,3],[0,2],[0,1,3],[0,2]])', False),
        ('is_bipartite([[],[]])', True),
    ]),
    'problems/is_palindrome_list.py': ('ll', [
        ('is_palindrome_list(build([1,2,2,1]))', True),
        ('is_palindrome_list(build([1,2]))', False),
        ('is_palindrome_list(build([1]))', True),
        ('is_palindrome_list(build([1,2,3,2,1]))', True),
    ]),
    'problems/is_power_of_two.py': (None, [
        ('is_power_of_two(16)', True),
        ('is_power_of_two(1)', True),
        ('is_power_of_two(0)', False),
        ('is_power_of_two(6)', False),
        ('is_power_of_two(-8)', False),
    ]),
    'problems/is_prime.py': (None, [
        ('is_prime(1)', False),
        ('is_prime(2)', True),
        ('is_prime(15)', False),
        ('is_prime(97)', True),
        ('is_prime(49)', False),
    ]),
    'problems/is_rotation.py': (None, [
        ('is_rotation("waterbottle","erbottlewat")', True),
        ('is_rotation("abc","acb")', False),
        ('is_rotation("ab","abc")', False),
        ('is_rotation("","")', True),
    ]),
    'problems/is_subsequence.py': (None, [
        ('is_subsequence("ace","abcde")', True),
        ('is_subsequence("aec","abcde")', False),
        ('is_subsequence("","x")', True),
        ('is_subsequence("a","")', False),
    ]),
    'problems/is_subtree.py': ('tree', [
        ('is_subtree(build_tree([3,4,5,1,2]),build_tree([4,1,2]))', True),
        ('is_subtree(build_tree([3,4,5,1,2,None,None,None,None,0]),build_tree([4,1,2]))', False),
    ]),
    'problems/is_toeplitz.py': (None, [
        ('is_toeplitz([[1,2,3],[4,1,2]])', True),
        ('is_toeplitz([[1,2],[2,2]])', False),
        ('is_toeplitz([[7]])', True),
    ]),
    'problems/is_valid_bst.py': ('tree', [
        ('is_valid_bst(build_tree([2,1,3]))', True),
        ('is_valid_bst(build_tree([5,1,4,None,None,3,6]))', False),
        ('is_valid_bst(None)', True),
        ('is_valid_bst(build_tree([2,2,2]))', False),
    ]),
    'problems/isomorphic.py': (None, [
        ('isomorphic("egg","add")', True),
        ('isomorphic("foo","bar")', False),
        ('isomorphic("paper","title")', True),
        ('isomorphic("ab","aa")', False),
    ]),
    'problems/jump_game_ii.py': (None, [
        ('jump_game_ii([2,3,1,1,4])', 2),
        ('jump_game_ii([2,3,0,1,4])', 2),
        ('jump_game_ii([0])', 0),
        ('jump_game_ii([1,1,1,1])', 3),
    ]),
    'problems/k_closest.py': (None, [
        ('k_closest([[1,3],[-2,2]],1)', [[-2, 2]]),
        ('k_closest([[3,3],[5,-1],[-2,4]],2)', [[3, 3], [-2, 4]]),
        ('k_closest([[0,1]],1)', [[0, 1]]),
    ]),
    'problems/k_closest_elements.py': (None, [
        ('k_closest_elements([1,2,3,4,5],4,3)', [1, 2, 3, 4]),
        ('k_closest_elements([1,2,3,4,5],4,-1)', [1, 2, 3, 4]),
        ('k_closest_elements([1,1,2,3,4,5],3,4)', [3, 4, 5]),
    ]),
    'problems/knapsack_01.py': (None, [
        ('knapsack_01([1,3,4,5],[1,4,5,7],7)', 9),
        ('knapsack_01([5],[10],4)', 0),
        ('knapsack_01([2,3],[3,4],5)', 7),
        ('knapsack_01([],[],10)', 0),
    ]),
    'problems/kth_largest.py': (None, [
        ('kth_largest([3,2,1,5,6,4],2)', 5),
        ('kth_largest([3,2,3,1,2,4,5,5,6],4)', 4),
        ('kth_largest([1],1)', 1),
    ]),
    'problems/kth_smallest_bst.py': ('tree', [
        ('kth_smallest_bst(build_tree([3,1,4,None,2]),1)', 1),
        ('kth_smallest_bst(build_tree([5,3,6,2,4,None,None,1]),3)', 3),
        ('kth_smallest_bst(build_tree([2,1,3]),3)', 3),
    ]),
    'problems/kth_smallest_matrix.py': (None, [
        ('kth_smallest_matrix([[1,5,9],[10,11,13],[12,13,15]],8)', 13),
        ('kth_smallest_matrix([[-5]],1)', -5),
        ('kth_smallest_matrix([[1,2],[1,3]],2)', 1),
    ]),
    'problems/largest_number.py': (None, [
        ('largest_number([3,30,34,5,9])', '9534330'),
        ('largest_number([10,2])', '210'),
        ('largest_number([0,0])', '0'),
    ]),
    'problems/largest_rectangle.py': (None, [
        ('largest_rectangle([2,1,5,6,2,3])', 10),
        ('largest_rectangle([2,4])', 4),
        ('largest_rectangle([5])', 5),
        ('largest_rectangle([])', 0),
    ]),
    'problems/last_stone_weight.py': (None, [
        ('last_stone_weight([2,7,4,1,8,1])', 1),
        ('last_stone_weight([1])', 1),
        ('last_stone_weight([3,3])', 0),
    ]),
    'problems/lca.py': ('tree', [
        ('lca(build_tree([3,5,1,6,2,0,8,None,None,7,4]),5,1)', 3),
        ('lca(build_tree([3,5,1,6,2,0,8,None,None,7,4]),5,4)', 5),
        ('lca(build_tree([1,2]),1,2)', 1),
    ]),
    'problems/lca_bst.py': ('tree', [
        ('lca_bst(build_tree([6,2,8,0,4,7,9,None,None,3,5]),2,8)', 6),
        ('lca_bst(build_tree([6,2,8,0,4,7,9,None,None,3,5]),2,4)', 2),
        ('lca_bst(build_tree([2,1]),2,1)', 2),
    ]),
    'problems/lcs.py': (None, [
        ('lcs("abcde","ace")', 3),
        ('lcs("abc","def")', 0),
        ('lcs("","abc")', 0),
        ('lcs("abc","abc")', 3),
    ]),
    'problems/leap_year.py': (None, [
        ('leap_year(2000)', True),
        ('leap_year(1900)', False),
        ('leap_year(2024)', True),
        ('leap_year(2023)', False),
    ]),
    'problems/lemonade_change.py': (None, [
        ('lemonade_change([5,5,5,10,20])', True),
        ('lemonade_change([5,5,10,10,20])', False),
        ('lemonade_change([10])', False),
        ('lemonade_change([])', True),
    ]),
    'problems/letter_combinations.py': (None, [
        ('letter_combinations("23")', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
        ('letter_combinations("")', []),
        ('letter_combinations("7")', ['p', 'q', 'r', 's']),
    ]),
    'problems/level_order.py': ('tree', [
        ('level_order(build_tree([3,9,20,None,None,15,7]))', [[3], [9, 20], [15, 7]]),
        ('level_order(None)', []),
        ('level_order(build_tree([1]))', [[1]]),
    ]),
    'problems/lis.py': (None, [
        ('lis([10,9,2,5,3,7,101,18])', 4),
        ('lis([0,1,0,3,2,3])', 4),
        ('lis([7,7,7])', 1),
        ('lis([])', 0),
    ]),
    'problems/longest_common_prefix.py': (None, [
        ('longest_common_prefix(["flower","flow","flight"])', 'fl'),
        ('longest_common_prefix(["dog","car"])', ''),
        ('longest_common_prefix(["a"])', 'a'),
        ('longest_common_prefix(["ab","ab"])', 'ab'),
    ]),
    'problems/longest_consecutive.py': (None, [
        ('longest_consecutive([100,4,200,1,3,2])', 4),
        ('longest_consecutive([])', 0),
        ('longest_consecutive([0,3,7,2,5,8,4,6,0,1])', 9),
        ('longest_consecutive([1,1,1])', 1),
    ]),
    'problems/longest_inc_path_matrix.py': (None, [
        ('longest_inc_path_matrix([[9,9,4],[6,6,8],[2,1,1]])', 4),
        ('longest_inc_path_matrix([[3,4,5],[3,2,6],[2,2,1]])', 4),
        ('longest_inc_path_matrix([[1]])', 1),
    ]),
    'problems/longest_ones.py': (None, [
        ('longest_ones([1,1,0,0,1,1,1,0,1],2)', 7),
        ('longest_ones([0,0,0],0)', 0),
        ('longest_ones([0,0],5)', 2),
        ('longest_ones([1,1],0)', 2),
    ]),
    'problems/longest_palindrome_substring.py': (None, [
        ('longest_palindrome_substring("babad")', 'bab'),
        ('longest_palindrome_substring("cbbd")', 'bb'),
        ('longest_palindrome_substring("a")', 'a'),
        ('longest_palindrome_substring("aaaa")', 'aaaa'),
    ]),
    'problems/longest_palindromic_subseq.py': (None, [
        ('longest_palindromic_subseq("bbbab")', 4),
        ('longest_palindromic_subseq("cbbd")', 2),
        ('longest_palindromic_subseq("a")', 1),
    ]),
    'problems/longest_repeating_replace.py': (None, [
        ('longest_repeating_replace("ABAB",2)', 4),
        ('longest_repeating_replace("AABABBA",1)', 4),
        ('longest_repeating_replace("A",0)', 1),
    ]),
    'problems/longest_unique_substring.py': (None, [
        ('longest_unique_substring("abcabcbb")', 3),
        ('longest_unique_substring("bbbbb")', 1),
        ('longest_unique_substring("pwwkew")', 3),
        ('longest_unique_substring("")', 0),
        ('longest_unique_substring("abba")', 2),
    ]),
    'problems/lru_cache.py': (None, [
        ('(lambda c: [c.put(1,1), c.put(2,2), c.get(1), c.put(3,3), c.get(2), c.put(4,4), c.get(1), c.get(3), c.get(4)])(LRUCache(2))', [None, None, 1, None, -1, None, -1, 3, 4]),
    ]),
    'problems/majority_element.py': (None, [
        ('majority_element([2,2,1,1,1,2,2])', 2),
        ('majority_element([3,2,3])', 3),
        ('majority_element([1])', 1),
    ]),
    'problems/max_activities.py': (None, [
        ('max_activities([1,3,0,5,8,5],[2,4,6,7,9,9])', 4),
        ('max_activities([1],[2])', 1),
        ('max_activities([1,2,3],[10,10,10])', 1),
        ('max_activities([],[])', 0),
    ]),
    'problems/max_area.py': (None, [
        ('max_area([1,8,6,2,5,4,8,3,7])', 49),
        ('max_area([1,1])', 1),
        ('max_area([4,3,2,1,4])', 16),
        ('max_area([0,0])', 0),
    ]),
    'problems/max_depth.py': ('tree', [
        ('max_depth(build_tree([3,9,20,None,None,15,7]))', 3),
        ('max_depth(None)', 0),
        ('max_depth(build_tree([1]))', 1),
        ('max_depth(build_tree([1,2,None,3]))', 3),
    ]),
    'problems/max_path_sum.py': ('tree', [
        ('max_path_sum(build_tree([1,2,3]))', 6),
        ('max_path_sum(build_tree([-10,9,20,None,None,15,7]))', 42),
        ('max_path_sum(build_tree([-3]))', -3),
    ]),
    'problems/max_product_subarray.py': (None, [
        ('max_product_subarray([2,3,-2,4])', 6),
        ('max_product_subarray([-2,0,-1])', 0),
        ('max_product_subarray([-2,3,-4])', 24),
        ('max_product_subarray([-2])', -2),
    ]),
    'problems/max_profit.py': (None, [
        ('max_profit([7,1,5,3,6,4])', 5),
        ('max_profit([7,6,4,3,1])', 0),
        ('max_profit([5])', 0),
        ('max_profit([1,2])', 1),
    ]),
    'problems/max_subarray.py': (None, [
        ('max_subarray([-2,1,-3,4,-1,2,1,-5,4])', 6),
        ('max_subarray([-3,-1,-2])', -1),
        ('max_subarray([5])', 5),
        ('max_subarray([1,2,3])', 6),
    ]),
    'problems/max_sum_circular.py': (None, [
        ('max_sum_circular([1,-2,3,-2])', 3),
        ('max_sum_circular([5,-3,5])', 10),
        ('max_sum_circular([-3,-2,-3])', -2),
    ]),
    'problems/max_sum_window.py': (None, [
        ('max_sum_window([2,1,5,1,3,2],3)', 9),
        ('max_sum_window([1,2],3)', -1),
        ('max_sum_window([-1,-2,-3],2)', -3),
        ('max_sum_window([4],1)', 4),
    ]),
    'problems/maximal_square.py': (None, [
        ('maximal_square(["10100","10111","11111","10010"])', 4),
        ('maximal_square(["01","10"])', 1),
        ('maximal_square(["0"])', 0),
        ('maximal_square(["11","11"])', 4),
    ]),
    'problems/median_two_sorted.py': (None, [
        ('median_two_sorted([1,3],[2])', 2.0),
        ('median_two_sorted([1,2],[3,4])', 2.5),
        ('median_two_sorted([0,0],[0,0])', 0.0),
        ('median_two_sorted([],[1])', 1.0),
    ]),
    'problems/meeting_rooms_ii.py': (None, [
        ('meeting_rooms_ii([[0,30],[5,10],[15,20]])', 2),
        ('meeting_rooms_ii([[7,10],[2,4]])', 1),
        ('meeting_rooms_ii([])', 0),
        ('meeting_rooms_ii([[1,5],[5,9]])', 1),
    ]),
    'problems/merge_intervals.py': (None, [
        ('merge_intervals([[1,3],[2,6],[8,10],[15,18]])', [[1, 6], [8, 10], [15, 18]]),
        ('merge_intervals([[1,4],[4,5]])', [[1, 5]]),
        ('merge_intervals([[1,10],[2,3]])', [[1, 10]]),
        ('merge_intervals([])', []),
    ]),
    'problems/merge_k_sorted.py': (None, [
        ('merge_k_sorted([[1,4,5],[1,3,4],[2,6]])', [1, 1, 2, 3, 4, 4, 5, 6]),
        ('merge_k_sorted([[],[1]])', [1]),
        ('merge_k_sorted([])', []),
    ]),
    'problems/merge_sort_impl.py': (None, [
        ('merge_sort_impl([5,1,4,2,3])', [1, 2, 3, 4, 5]),
        ('merge_sort_impl([])', []),
        ('merge_sort_impl([3,3,1])', [1, 3, 3]),
    ]),
    'problems/merge_sorted.py': (None, [
        ('merge_sorted([1,3,5],[2,4,6])', [1, 2, 3, 4, 5, 6]),
        ('merge_sorted([],[1])', [1]),
        ('merge_sorted([1,1],[1])', [1, 1, 1]),
        ('merge_sorted([],[])', []),
    ]),
    'problems/merge_two_lists.py': ('ll', [
        ('to_list(merge_two_lists(build([1,2,4]),build([1,3,4])))', [1, 1, 2, 3, 4, 4]),
        ('to_list(merge_two_lists(build([]),build([])))', []),
        ('to_list(merge_two_lists(build([]),build([0])))', [0]),
    ]),
    'problems/middle_node.py': ('ll', [
        ('to_list(middle_node(build([1,2,3,4,5])))', [3, 4, 5]),
        ('to_list(middle_node(build([1,2,3,4])))', [3, 4]),
        ('to_list(middle_node(build([9])))', [9]),
    ]),
    'problems/min_coins_greedy.py': (None, [
        ('min_coins_greedy(93)', 5),
        ('min_coins_greedy(0)', 0),
        ('min_coins_greedy(2000)', 1),
        ('min_coins_greedy(11)', 2),
    ]),
    'problems/min_cost_climbing.py': (None, [
        ('min_cost_climbing([10,15,20])', 15),
        ('min_cost_climbing([1,100,1,1,1,100,1,1,100,1])', 6),
        ('min_cost_climbing([5,3])', 3),
    ]),
    'problems/min_path_sum.py': (None, [
        ('min_path_sum([[1,3,1],[1,5,1],[4,2,1]])', 7),
        ('min_path_sum([[1,2],[1,1]])', 3),
        ('min_path_sum([[5]])', 5),
    ]),
    'problems/min_platforms.py': (None, [
        ('min_platforms([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000])', 3),
        ('min_platforms([900],[910])', 1),
        ('min_platforms([900,910],[910,920])', 2),
    ]),
    'problems/min_stack.py': (None, [
        ('(lambda s: [s.push(3), s.push(1), s.get_min(), s.pop(), s.get_min()])(MinStack())', [None, None, 1, 1, 3]),
        ('(lambda s: [s.push(2), s.push(2), s.pop(), s.get_min()])(MinStack())', [None, None, 2, 2]),
    ]),
    'problems/min_subarray_len.py': (None, [
        ('min_subarray_len(7,[2,3,1,2,4,3])', 2),
        ('min_subarray_len(4,[1,4,4])', 1),
        ('min_subarray_len(11,[1,1,1,1])', 0),
        ('min_subarray_len(1,[1])', 1),
    ]),
    'problems/min_window.py': (None, [
        ('min_window("ADOBECODEBANC","ABC")', 'BANC'),
        ('min_window("a","a")', 'a'),
        ('min_window("a","aa")', ''),
        ('min_window("aa","aa")', 'aa'),
    ]),
    'problems/missing_number.py': (None, [
        ('missing_number([3,0,1])', 2),
        ('missing_number([0,1])', 2),
        ('missing_number([1])', 0),
        ('missing_number([9,6,4,2,3,5,7,0,1])', 8),
    ]),
    'problems/most_frequent_word.py': (None, [
        ('most_frequent_word(["b","a","b","a","c"])', 'a'),
        ('most_frequent_word(["x"])', 'x'),
        ('most_frequent_word(["z","z","y"])', 'z'),
    ]),
    'problems/move_zeroes.py': (None, [
        ('move_zeroes([0,1,0,3,12])', [1, 3, 12, 0, 0]),
        ('move_zeroes([0,0])', [0, 0]),
        ('move_zeroes([1,2])', [1, 2]),
        ('move_zeroes([4])', [4]),
    ]),
    'problems/mst_weight.py': (None, [
        ('mst_weight(4,[[0,1,10],[0,2,6],[0,3,5],[1,3,15],[2,3,4]])', 19),
        ('mst_weight(1,[])', 0),
        ('mst_weight(3,[[0,1,1],[1,2,2],[0,2,3]])', 3),
    ]),
    'problems/multiply_strings.py': (None, [
        ('multiply_strings("123","456")', '56088'),
        ('multiply_strings("0","0")', '0'),
        ('multiply_strings("2","3")', '6'),
        ('multiply_strings("99","99")', '9801'),
    ]),
    'problems/my_atoi.py': (None, [
        ('my_atoi("  -42abc")', -42),
        ('my_atoi("4193 with words")', 4193),
        ('my_atoi("words 5")', 0),
        ('my_atoi("")', 0),
        ('my_atoi("+7")', 7),
    ]),
    'problems/my_pow.py': (None, [
        ('my_pow(2.0,10)', 1024.0),
        ('my_pow(2.0,-2)', 0.25),
        ('my_pow(2,0)', 1.0),
        ('my_pow(3.0,3)', 27.0),
    ]),
    'problems/my_queue.py': (None, [
        ('(lambda q: [q.push(1), q.push(2), q.peek(), q.pop(), q.empty()])(MyQueue())', [None, None, 1, 1, False]),
        ('(lambda q: [q.push(5), q.pop(), q.empty()])(MyQueue())', [None, 5, True]),
    ]),
    'problems/my_sqrt.py': (None, [
        ('my_sqrt(8)', 2),
        ('my_sqrt(0)', 0),
        ('my_sqrt(1)', 1),
        ('my_sqrt(16)', 4),
        ('my_sqrt(2147395599)', 46339),
    ]),
    'problems/n_queens_count.py': (None, [
        ('n_queens_count(4)', 2),
        ('n_queens_count(1)', 1),
        ('n_queens_count(3)', 0),
        ('n_queens_count(6)', 4),
        ('n_queens_count(8)', 92),
    ]),
    'problems/ncr_mod.py': (None, [
        ('ncr_mod(5,2)', 10),
        ('ncr_mod(10,0)', 1),
        ('ncr_mod(52,5)', 2598960),
        ('ncr_mod(3,5)', 0),
    ]),
    'problems/network_delay.py': (None, [
        ('network_delay([[2,1,1],[2,3,1],[3,4,1]],4,2)', 2),
        ('network_delay([[1,2,1]],2,1)', 1),
        ('network_delay([[1,2,1]],2,2)', -1),
        ('network_delay([[1,2,5],[1,3,1],[3,2,1]],3,1)', 2),
    ]),
    'problems/next_greater.py': (None, [
        ('next_greater([4,5,2,25])', [5, 25, 25, -1]),
        ('next_greater([13,7,6,12])', [-1, 12, 12, -1]),
        ('next_greater([3,3])', [-1, -1]),
        ('next_greater([])', []),
    ]),
    'problems/next_permutation.py': (None, [
        ('next_permutation([1,2,3])', [1, 3, 2]),
        ('next_permutation([3,2,1])', [1, 2, 3]),
        ('next_permutation([1,1,5])', [1, 5, 1]),
        ('next_permutation([1,3,2])', [2, 1, 3]),
    ]),
    'problems/non_overlapping_intervals.py': (None, [
        ('non_overlapping_intervals([[1,2],[2,3],[3,4],[1,3]])', 1),
        ('non_overlapping_intervals([[1,2],[1,2],[1,2]])', 2),
        ('non_overlapping_intervals([[1,2],[2,3]])', 0),
    ]),
    'problems/num_islands.py': (None, [
        ('num_islands(["11000","11000","00100","00011"])', 3),
        ('num_islands(["000"])', 0),
        ('num_islands(["111","111"])', 1),
        ('num_islands([])', 0),
    ]),
    'problems/number_of_provinces.py': (None, [
        ('number_of_provinces([[1,1,0],[1,1,0],[0,0,1]])', 2),
        ('number_of_provinces([[1,0,0],[0,1,0],[0,0,1]])', 3),
        ('number_of_provinces([[1,1],[1,1]])', 1),
    ]),
    'problems/pacific_atlantic.py': (None, [
        ('pacific_atlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])', [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),
        ('pacific_atlantic([[1]])', [[0, 0]]),
    ]),
    'problems/palindrome_number.py': (None, [
        ('palindrome_number(121)', True),
        ('palindrome_number(-121)', False),
        ('palindrome_number(10)', False),
        ('palindrome_number(0)', True),
        ('palindrome_number(12321)', True),
    ]),
    'problems/palindrome_partitions.py': (None, [
        ('palindrome_partitions("aab")', [['a', 'a', 'b'], ['aa', 'b']]),
        ('palindrome_partitions("a")', [['a']]),
        ('len(palindrome_partitions("aaa"))', 4),
    ]),
    'problems/palindrome_rec.py': (None, [
        ('palindrome_rec("level")', True),
        ('palindrome_rec("ab")', False),
        ('palindrome_rec("")', True),
        ('palindrome_rec("abba")', True),
    ]),
    'problems/palindromic_substrings.py': (None, [
        ('palindromic_substrings("abc")', 3),
        ('palindromic_substrings("aaa")', 6),
        ('palindromic_substrings("a")', 1),
    ]),
    'problems/partition_equal_subset.py': (None, [
        ('partition_equal_subset([1,5,11,5])', True),
        ('partition_equal_subset([1,2,3,5])', False),
        ('partition_equal_subset([2,2])', True),
        ('partition_equal_subset([1])', False),
    ]),
    'problems/partition_labels.py': (None, [
        ('partition_labels("ababcbacadefegdehijhklij")', [9, 7, 8]),
        ('partition_labels("eccbbbbdec")', [10]),
        ('partition_labels("abc")', [1, 1, 1]),
    ]),
    'problems/path_exists.py': (None, [
        ('path_exists(3,[[0,1],[1,2],[2,0]],0,2)', True),
        ('path_exists(6,[[0,1],[0,2],[3,5],[5,4],[4,3]],0,5)', False),
        ('path_exists(1,[],0,0)', True),
    ]),
    'problems/perfect_squares.py': (None, [
        ('perfect_squares(12)', 3),
        ('perfect_squares(13)', 2),
        ('perfect_squares(1)', 1),
        ('perfect_squares(7)', 4),
    ]),
    'problems/permutations.py': (None, [
        ('permutations([1,2,3])', [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ('permutations([1])', [[1]]),
        ('len(permutations([1,2,3,4]))', 24),
    ]),
    'problems/permutations_unique.py': (None, [
        ('permutations_unique([1,1,2])', [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ('permutations_unique([1,2])', [[1, 2], [2, 1]]),
        ('permutations_unique([2,2])', [[2, 2]]),
    ]),
    'problems/plus_one.py': (None, [
        ('plus_one([1,2,9])', [1, 3, 0]),
        ('plus_one([9,9])', [1, 0, 0]),
        ('plus_one([0])', [1]),
        ('plus_one([4,3,2,1])', [4, 3, 2, 2]),
    ]),
    'problems/power_of_three.py': (None, [
        ('power_of_three(27)', True),
        ('power_of_three(0)', False),
        ('power_of_three(45)', False),
        ('power_of_three(1)', True),
    ]),
    'problems/product_except_self.py': (None, [
        ('product_except_self([1,2,3,4])', [24, 12, 8, 6]),
        ('product_except_self([-1,1,0,-3,3])', [0, 0, 9, 0, 0]),
        ('product_except_self([2,5])', [5, 2]),
    ]),
    'problems/pyramid.py': (None, [
        ('pyramid(3)', ['1', '1 2', '1 2 3']),
        ('pyramid(1)', ['1']),
        ('pyramid(4)[3]', '1 2 3 4'),
    ]),
    'problems/randomized_set.py': (None, [
        ('(lambda s: [s.insert(1), s.insert(1), s.remove(2), s.insert(2), s.remove(1), s.insert(2)])(RandomizedSet())', [True, False, False, True, True, False]),
        ('(lambda s: [s.insert(5), s.get_random()])(RandomizedSet())', [True, 5]),
    ]),
    'problems/range_bitwise_and.py': (None, [
        ('range_bitwise_and(5,7)', 4),
        ('range_bitwise_and(0,0)', 0),
        ('range_bitwise_and(1,2147483647)', 0),
        ('range_bitwise_and(6,6)', 6),
    ]),
    'problems/range_sum_2d.py': (None, [
        ('range_sum_2d([[1,2],[3,4]],[(0,0,1,1)])', [10]),
        ('range_sum_2d([[1,2],[3,4]],[(1,0,1,1)])', [7]),
        ('range_sum_2d([[5]],[(0,0,0,0)])', [5]),
    ]),
    'problems/range_sum_queries.py': (None, [
        ('range_sum_queries([2,4,1,3],[[0,1],[1,3],[2,2]])', [6, 8, 1]),
        ('range_sum_queries([5],[[0,0]])', [5]),
        ('range_sum_queries([1,2,3],[[0,2]])', [6]),
    ]),
    'problems/ransom_note.py': (None, [
        ('ransom_note("aa","aab")', True),
        ('ransom_note("aa","ab")', False),
        ('ransom_note("","x")', True),
    ]),
    'problems/redundant_connection.py': (None, [
        ('redundant_connection([[1,2],[1,3],[2,3]])', [2, 3]),
        ('redundant_connection([[1,2],[2,3],[3,4],[1,4],[1,5]])', [1, 4]),
    ]),
    'problems/regex_match.py': (None, [
        ('regex_match("aa","a")', False),
        ('regex_match("aa","a*")', True),
        ('regex_match("ab",".*")', True),
        ('regex_match("aab","c*a*b")', True),
        ('regex_match("mississippi","mis*is*p*.")', False),
    ]),
    'problems/remove_duplicates.py': (None, [
        ('remove_duplicates([])', 0),
        ('remove_duplicates([1,1,1])', 1),
        ('remove_duplicates([1,2,3])', 3),
        ('[(k := remove_duplicates(a := [0,0,1,1,1,2,2,3,3,4])), a[:k]]', [5, [0, 1, 2, 3, 4]]),
    ]),
    'problems/remove_element.py': (None, [
        ('remove_element([3,2,2,3],3)', 2),
        ('remove_element([1,2],5)', 2),
        ('remove_element([4,4],4)', 0),
        ('remove_element([],1)', 0),
    ]),
    'problems/remove_k_digits.py': (None, [
        ('remove_k_digits("1432219",3)', '1219'),
        ('remove_k_digits("10200",1)', '200'),
        ('remove_k_digits("10",2)', '0'),
        ('remove_k_digits("12345",2)', '123'),
    ]),
    'problems/remove_nth_from_end.py': ('ll', [
        ('to_list(remove_nth_from_end(build([1,2,3,4,5]),2))', [1, 2, 3, 5]),
        ('to_list(remove_nth_from_end(build([1]),1))', []),
        ('to_list(remove_nth_from_end(build([1,2]),2))', [2]),
    ]),
    'problems/remove_vowels.py': (None, [
        ('remove_vowels("Infosys")', 'nfsys'),
        ('remove_vowels("AEIOU")', ''),
        ('remove_vowels("xyz")', 'xyz'),
    ]),
    'problems/reorder_list.py': ('ll', [
        ('(lambda h: (reorder_list(h), to_list(h))[1])(build([1,2,3,4]))', [1, 4, 2, 3]),
        ('(lambda h: (reorder_list(h), to_list(h))[1])(build([1,2,3,4,5]))', [1, 5, 2, 4, 3]),
        ('(lambda h: (reorder_list(h), to_list(h))[1])(build([1]))', [1]),
    ]),
    'problems/reorganize_string.py': (None, [
        ('(lambda r: r != "" and all(a != b for a, b in zip(r, r[1:])) and sorted(r) == sorted("aab"))(reorganize_string("aab"))', True),
        ('reorganize_string("aaab")', ''),
        ('reorganize_string("a")', 'a'),
    ]),
    'problems/restore_ip.py': (None, [
        ('restore_ip("25525511135")', ['255.255.11.135', '255.255.111.35']),
        ('restore_ip("0000")', ['0.0.0.0']),
        ('restore_ip("1")', []),
    ]),
    'problems/reverse_bits.py': (None, [
        ('reverse_bits(43261596)', 964176192),
        ('reverse_bits(0)', 0),
        ('reverse_bits(1)', 2147483648),
    ]),
    'problems/reverse_integer.py': (None, [
        ('reverse_integer(123)', 321),
        ('reverse_integer(-123)', -321),
        ('reverse_integer(120)', 21),
        ('reverse_integer(1534236469)', 0),
    ]),
    'problems/reverse_k_group.py': ('ll', [
        ('to_list(reverse_k_group(build([1,2,3,4,5]),2))', [2, 1, 4, 3, 5]),
        ('to_list(reverse_k_group(build([1,2,3,4,5]),3))', [3, 2, 1, 4, 5]),
        ('to_list(reverse_k_group(build([1,2]),3))', [1, 2]),
        ('to_list(reverse_k_group(build([1,2,3]),1))', [1, 2, 3]),
    ]),
    'problems/reverse_list.py': ('ll', [
        ('to_list(reverse_list(build([1,2,3,4,5])))', [5, 4, 3, 2, 1]),
        ('to_list(reverse_list(build([])))', []),
        ('to_list(reverse_list(build([7])))', [7]),
    ]),
    'problems/reverse_number.py': (None, [
        ('reverse_number(123)', 321),
        ('reverse_number(1200)', 21),
        ('reverse_number(0)', 0),
        ('reverse_number(5)', 5),
    ]),
    'problems/reverse_words.py': (None, [
        ('reverse_words("  the sky  is blue ")', 'blue is sky the'),
        ('reverse_words("a")', 'a'),
        ('reverse_words("   ")', ''),
    ]),
    'problems/right_side_view.py': ('tree', [
        ('right_side_view(build_tree([1,2,3,None,5,None,4]))', [1, 3, 4]),
        ('right_side_view(None)', []),
        ('right_side_view(build_tree([1,2]))', [1, 2]),
    ]),
    'problems/roman_to_int.py': (None, [
        ('roman_to_int("III")', 3),
        ('roman_to_int("LVIII")', 58),
        ('roman_to_int("MCMXCIV")', 1994),
        ('roman_to_int("IV")', 4),
    ]),
    'problems/rotate_list.py': ('ll', [
        ('to_list(rotate_list(build([1,2,3,4,5]),2))', [4, 5, 1, 2, 3]),
        ('to_list(rotate_list(build([0,1,2]),4))', [2, 0, 1]),
        ('to_list(rotate_list(build([1]),99))', [1]),
    ]),
    'problems/rotate_matrix.py': (None, [
        ('rotate_matrix([[1,2],[3,4]])', [[3, 1], [4, 2]]),
        ('rotate_matrix([[1]])', [[1]]),
        ('rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])', [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ]),
    'problems/rotate_right.py': (None, [
        ('rotate_right([1,2,3,4,5,6,7],3)', [5, 6, 7, 1, 2, 3, 4]),
        ('rotate_right([1,2],5)', [2, 1]),
        ('rotate_right([],3)', []),
        ('rotate_right([1,2,3],0)', [1, 2, 3]),
    ]),
    'problems/rotting_oranges.py': (None, [
        ('rotting_oranges([[2,1,1],[1,1,0],[0,1,1]])', 4),
        ('rotting_oranges([[2,1,1],[0,1,1],[1,0,1]])', -1),
        ('rotting_oranges([[0,2]])', 0),
        ('rotting_oranges([[1]])', -1),
    ]),
    'problems/running_median.py': (None, [
        ('running_median([5,15,1,3])', [5, 10.0, 5, 4.0]),
        ('running_median([2])', [2]),
        ('running_median([1,1,1])', [1, 1.0, 1]),
    ]),
    'problems/search_insert.py': (None, [
        ('search_insert([1,3,5,6],5)', 2),
        ('search_insert([1,3,5,6],2)', 1),
        ('search_insert([1,3,5,6],7)', 4),
        ('search_insert([1,3,5,6],0)', 0),
    ]),
    'problems/search_matrix.py': (None, [
        ('search_matrix([[1,3,5],[7,9,11]],9)', True),
        ('search_matrix([[1,3,5],[7,9,11]],4)', False),
        ('search_matrix([[1]],1)', True),
        ('search_matrix([],1)', False),
    ]),
    'problems/search_rotated.py': (None, [
        ('search_rotated([4,5,6,7,0,1,2],0)', 4),
        ('search_rotated([4,5,6,7,0,1,2],3)', -1),
        ('search_rotated([1],1)', 0),
        ('search_rotated([3,1],1)', 1),
    ]),
    'problems/second_largest.py': (None, [
        ('second_largest([3,1,4,4,2])', 3),
        ('second_largest([5,5])', -1),
        ('second_largest([1,2])', 1),
        ('second_largest([-1,-2,-3])', -2),
        ('second_largest([7])', -1),
    ]),
    'problems/serialize_tree.py': ('tree', [
        ('serialize_tree(build_tree([1,2,3,None,None,4,5]))', '1,2,#,#,3,4,#,#,5,#,#'),
        ('serialize_tree(deserialize_tree("1,2,#,#,3,4,#,#,5,#,#"))', '1,2,#,#,3,4,#,#,5,#,#'),
        ('serialize_tree(None)', '#'),
    ]),
    'problems/set_matrix_zeroes.py': (None, [
        ('set_matrix_zeroes([[1,1,1],[1,0,1],[1,1,1]])', [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ('set_matrix_zeroes([[0,1],[1,1]])', [[0, 0], [0, 1]]),
        ('set_matrix_zeroes([[1]])', [[1]]),
    ]),
    'problems/ship_capacity.py': (None, [
        ('ship_capacity([1,2,3,4,5,6,7,8,9,10],5)', 15),
        ('ship_capacity([3,2,2,4,1,4],3)', 6),
        ('ship_capacity([1,2,3,1,1],4)', 3),
        ('ship_capacity([5],1)', 5),
    ]),
    'problems/shortest_path_grid.py': (None, [
        ('shortest_path_grid(["..#","...","#.."])', 4),
        ('shortest_path_grid(["."])', 0),
        ('shortest_path_grid([".#","#."])', -1),
        ('shortest_path_grid(["#."])', -1),
    ]),
    'problems/single_number.py': (None, [
        ('single_number([4,1,2,1,2])', 4),
        ('single_number([2,2,1])', 1),
        ('single_number([7])', 7),
    ]),
    'problems/single_number_ii.py': (None, [
        ('single_number_ii([2,2,3,2])', 3),
        ('single_number_ii([0,1,0,1,0,1,99])', 99),
        ('single_number_ii([-2,-2,1,-2])', 1),
        ('single_number_ii([5])', 5),
    ]),
    'problems/sliding_window_max.py': (None, [
        ('sliding_window_max([1,3,-1,-3,5,3,6,7],3)', [3, 3, 5, 5, 6, 7]),
        ('sliding_window_max([1],1)', [1]),
        ('sliding_window_max([9,8,7],3)', [9]),
        ('sliding_window_max([1,2,3],1)', [1, 2, 3]),
    ]),
    'problems/sort_by_frequency.py': (None, [
        ('sort_by_frequency([2,3,1,3,2])', [2, 2, 3, 3, 1]),
        ('sort_by_frequency([1,1,1,2,2,3])', [1, 1, 1, 2, 2, 3]),
        ('sort_by_frequency([])', []),
    ]),
    'problems/sort_by_length.py': (None, [
        ('sort_by_length(["pear","fig","apple","kiwi"])', ['fig', 'kiwi', 'pear', 'apple']),
        ('sort_by_length([])', []),
        ('sort_by_length(["b","a"])', ['a', 'b']),
    ]),
    'problems/sort_colors.py': (None, [
        ('sort_colors([2,0,2,1,1,0])', [0, 0, 1, 1, 2, 2]),
        ('sort_colors([1])', [1]),
        ('sort_colors([2,2,0])', [0, 2, 2]),
        ('sort_colors([])', []),
    ]),
    'problems/sort_list.py': ('ll', [
        ('to_list(sort_list(build([4,2,1,3])))', [1, 2, 3, 4]),
        ('to_list(sort_list(build([-1,5,3,4,0])))', [-1, 0, 3, 4, 5]),
        ('to_list(sort_list(build([])))', []),
    ]),
    'problems/spiral_order.py': (None, [
        ('spiral_order([[1,2,3],[4,5,6],[7,8,9]])', [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ('spiral_order([[1,2,3,4]])', [1, 2, 3, 4]),
        ('spiral_order([[1],[2],[3]])', [1, 2, 3]),
        ('spiral_order([[1,2],[3,4]])', [1, 2, 4, 3]),
    ]),
    'problems/stock_cooldown.py': (None, [
        ('stock_cooldown([1,2,3,0,2])', 3),
        ('stock_cooldown([1])', 0),
        ('stock_cooldown([6,1,3,2,4,7])', 6),
    ]),
    'problems/subarray_sum_k.py': (None, [
        ('subarray_sum_k([1,1,1],2)', 2),
        ('subarray_sum_k([1,2,3],3)', 2),
        ('subarray_sum_k([1,-1,0],0)', 3),
        ('subarray_sum_k([],0)', 0),
    ]),
    'problems/subarrays_div_k.py': (None, [
        ('subarrays_div_k([4,5,0,-2,-3,1],5)', 7),
        ('subarrays_div_k([5],9)', 0),
        ('subarrays_div_k([1,2,3],1)', 6),
    ]),
    'problems/subsets.py': (None, [
        ('subsets([1,2,3])', [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
        ('subsets([])', [[]]),
        ('len(subsets(list(range(5))))', 32),
    ]),
    'problems/subsets_bitmask.py': (None, [
        ('subsets_bitmask([1,2,3])', [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ('subsets_bitmask([])', [[]]),
        ('len(subsets_bitmask([1,2,3,4]))', 16),
    ]),
    'problems/subsets_with_dup.py': (None, [
        ('subsets_with_dup([1,2,2])', [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
        ('subsets_with_dup([0])', [[], [0]]),
        ('subsets_with_dup([2,2,2])', [[], [2], [2, 2], [2, 2, 2]]),
    ]),
    'problems/surrounded_regions.py': (None, [
        ('surrounded_regions(["XXXX","XOOX","XXOX","XOXX"])', ['XXXX', 'XXXX', 'XXXX', 'XOXX']),
        ('surrounded_regions(["X"])', ['X']),
        ('surrounded_regions(["OO","OO"])', ['OO', 'OO']),
    ]),
    'problems/swap_pairs.py': ('ll', [
        ('to_list(swap_pairs(build([1,2,3,4])))', [2, 1, 4, 3]),
        ('to_list(swap_pairs(build([1])))', [1]),
        ('to_list(swap_pairs(build([])))', []),
        ('to_list(swap_pairs(build([1,2,3])))', [2, 1, 3]),
    ]),
    'problems/target_sum.py': (None, [
        ('target_sum([1,1,1,1,1],3)', 5),
        ('target_sum([1],1)', 1),
        ('target_sum([1],2)', 0),
        ('target_sum([0,0,1],1)', 4),
    ]),
    'problems/task_scheduler.py': (None, [
        ('task_scheduler(["A","A","A","B","B","B"],2)', 8),
        ('task_scheduler(["A","A","A","B","B","B"],0)', 6),
        ('task_scheduler(["A","A","A","A","A","A","B","C","D","E","F","G"],2)', 16),
    ]),
    'problems/three_sum.py': (None, [
        ('three_sum([-1,0,1,2,-1,-4])', [[-1, -1, 2], [-1, 0, 1]]),
        ('three_sum([0,0,0,0])', [[0, 0, 0]]),
        ('three_sum([1,2])', []),
        ('three_sum([1,2,-2,-1])', []),
    ]),
    'problems/three_sum_closest.py': (None, [
        ('three_sum_closest([-1,2,1,-4],1)', 2),
        ('three_sum_closest([0,0,0],1)', 0),
        ('three_sum_closest([1,1,1,0],-100)', 2),
    ]),
    'problems/top_k_frequent.py': (None, [
        ('top_k_frequent([1,1,1,2,2,3],2)', [1, 2]),
        ('top_k_frequent([1],1)', [1]),
        ('top_k_frequent([4,4,5,5,6],2)', [4, 5]),
    ]),
    'problems/trailing_zeros.py': (None, [
        ('trailing_zeros(25)', 6),
        ('trailing_zeros(5)', 1),
        ('trailing_zeros(100)', 24),
        ('trailing_zeros(4)', 0),
    ]),
    'problems/trapping_rain.py': (None, [
        ('trapping_rain([0,1,0,2,1,0,1,3,2,1,2,1])', 6),
        ('trapping_rain([4,2,0,3,2,5])', 9),
        ('trapping_rain([])', 0),
        ('trapping_rain([1,2,3])', 0),
    ]),
    'problems/triangle_min_path.py': (None, [
        ('triangle_min_path([[2],[3,4],[6,5,7],[4,1,8,3]])', 11),
        ('triangle_min_path([[-10]])', -10),
    ]),
    'problems/trie_class.py': (None, [
        ('(lambda t: [t.insert("apple"), t.search("apple"), t.search("app"), t.starts_with("app")])(Trie())', [None, True, False, True]),
        ('(lambda t: [t.insert("a"), t.search("b"), t.starts_with("")])(Trie())', [None, False, True]),
    ]),
    'problems/two_city_cost.py': (None, [
        ('two_city_cost([[10,20],[30,200],[400,50],[30,20]])', 110),
        ('two_city_cost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])', 1859),
    ]),
    'problems/two_sum.py': (None, [
        ('two_sum([2,7,11,15],9)', [0, 1]),
        ('two_sum([3,2,4],6)', [1, 2]),
        ('two_sum([3,3],6)', [0, 1]),
        ('two_sum([-1,-2,-3,-4,-5],-8)', [2, 4]),
    ]),
    'problems/two_sum_sorted.py': (None, [
        ('two_sum_sorted([2,7,11,15],9)', [0, 1]),
        ('two_sum_sorted([1,2,3,4],8)', [-1, -1]),
        ('two_sum_sorted([3,3],6)', [0, 1]),
        ('two_sum_sorted([5],5)', [-1, -1]),
    ]),
    'problems/ugly_number_ii.py': (None, [
        ('ugly_number_ii(10)', 12),
        ('ugly_number_ii(1)', 1),
        ('ugly_number_ii(15)', 24),
    ]),
    'problems/unique_bst.py': (None, [
        ('unique_bst(3)', 5),
        ('unique_bst(1)', 1),
        ('unique_bst(5)', 42),
    ]),
    'problems/unique_paths.py': (None, [
        ('unique_paths(3,7)', 28),
        ('unique_paths(3,2)', 3),
        ('unique_paths(1,5)', 1),
        ('unique_paths(3,3)', 6),
    ]),
    'problems/unique_paths_obstacles.py': (None, [
        ('unique_paths_obstacles([[0,0,0],[0,1,0],[0,0,0]])', 2),
        ('unique_paths_obstacles([[0,1],[0,0]])', 1),
        ('unique_paths_obstacles([[1]])', 0),
        ('unique_paths_obstacles([[0]])', 1),
    ]),
    'problems/valid_palindrome.py': (None, [
        ('valid_palindrome("A man, a plan, a canal: Panama")', True),
        ('valid_palindrome("race a car")', False),
        ('valid_palindrome("")', True),
        ('valid_palindrome(" ")', True),
        ('valid_palindrome("0P")', False),
    ]),
    'problems/valid_palindrome_ii.py': (None, [
        ('valid_palindrome_ii("aba")', True),
        ('valid_palindrome_ii("abca")', True),
        ('valid_palindrome_ii("abc")', False),
        ('valid_palindrome_ii("")', True),
    ]),
    'problems/valid_parens.py': (None, [
        ('valid_parens("()[]{}")', True),
        ('valid_parens("(]")', False),
        ('valid_parens("([)]")', False),
        ('valid_parens("{[]}")', True),
        ('valid_parens("")', True),
        ('valid_parens("((")', False),
        ('valid_parens(")")', False),
    ]),
    'problems/valid_sudoku.py': (None, [
        ('valid_sudoku(["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"])', True),
        ('valid_sudoku(["83..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"])', False),
        ('valid_sudoku(["........."] * 9)', True),
    ]),
    'problems/word_break.py': (None, [
        ('word_break("leetcode",["leet","code"])', True),
        ('word_break("applepenapple",["apple","pen"])', True),
        ('word_break("catsandog",["cats","dog","sand","and","cat"])', False),
    ]),
    'problems/word_dictionary.py': (None, [
        ('(lambda d: [d.add_word("bad"), d.add_word("dad"), d.add_word("mad"), d.search("pad"), d.search("bad"), d.search(".ad"), d.search("b..")])(WordDictionary())', [None, None, None, False, True, True, True]),
    ]),
    'problems/word_ladder.py': (None, [
        ('word_ladder("hit","cog",["hot","dot","dog","lot","log","cog"])', 5),
        ('word_ladder("hit","cog",["hot","dot","dog","lot","log"])', 0),
        ('word_ladder("a","c",["a","b","c"])', 2),
    ]),
    'problems/word_pattern.py': (None, [
        ('word_pattern("abba","dog cat cat dog")', True),
        ('word_pattern("abba","dog cat cat fish")', False),
        ('word_pattern("aaaa","dog cat cat dog")', False),
        ('word_pattern("abba","dog dog dog dog")', False),
    ]),
    'problems/word_search.py': (None, [
        ('word_search(["ABCE","SFCS","ADEE"],"ABCCED")', True),
        ('word_search(["ABCE","SFCS","ADEE"],"SEE")', True),
        ('word_search(["ABCE","SFCS","ADEE"],"ABCB")', False),
    ]),
    'problems/zigzag_level_order.py': ('tree', [
        ('zigzag_level_order(build_tree([3,9,20,None,None,15,7]))', [[3], [20, 9], [15, 7]]),
        ('zigzag_level_order(None)', []),
        ('zigzag_level_order(build_tree([1,2,3,4,5,6,7]))', [[1], [3, 2], [4, 5, 6, 7]]),
    ]),
}

SNIPPETS = [
    ('concepts/c1_1_extra1.py', 'compile-only'),
    ('concepts/c1_1_extra2.py', None),
    ('concepts/c3_1_extra1.py', None),
    ('concepts/c3_3_extra1.py', None),
    ('concepts/c5_1_extra1.py', None),
]
