SEQ_1 = 'GAGCCTACTAACGGGAT'
SEQ_2 = 'CATCGTAATGACGGCCT'

SEQ_3 = 'TATATTGCAAGAGATGATTGGCTACGCCGCAGAACACAATCTTAGCCTTACGCTGTCCTCTCCATAACGAAACCTCCTGTCGAGAGTCATTCGTCCTTGTAAGTACAGCGAAGGGACAGGCCACAGACTGAACCGTAATGTCCATTAACCTGTTGGAAATGTAGAAGAGTGCGAGCCTTGGACATCTTTGTAACATTCTGATGTATGGGAGTACAACTTTCTACATGATTTGTCTTTGCATATAAGGCGCACGCACCGATGGTAGAGATCCTCATTAATCGGTTCGTCACATACTGCGTTCATGCGTACTTCCGGTTGATGCACTAGTAGCGATCTGCTCGGGAGGATATAGCTTCCGCTGTAAGGCTCTCCAGGCGACTGAGTTTATGCCAGATTGCGCTGGTCACAATCGTACTGCATTCCCTCATTTCTAAAGGGGTATACACACCAAGACCGACCTACAGCCAATCGGACAATGACCTATTCGCAACTACGTGGTCAGCACGGAGAGGCAAAATCACGCCCTAGCGAGGTATGAAACGCACGGTCCTTAGCGTTCATGCGAATATTCCCTGGTCAGAGTAGTACGGCTGCCACGACTCATTTGTCACGTGCAGTAAACTGGAGAGAAGAACTGTCTAGCTACGAGTGGACCCAACCGGCCACCAACCATGCTCTGGGCCGCAATAAAATGCAAGAGATCGTAACCGAATATTACCACATAGAACCATGAGAATGTCCTCTCCCCCTATACAAGGGCTGTCCTTGGAGTTCTAGTGCCTGATTAGTAGTTACATTGAAAATTAGCTGCATATCTTCCAGGGCGAGCAGTATCACCTACGCCCAGCAGCTGTAAGATGACAGTAAGACTCTCGAGTTCGCACAAGCAGTTTACAGAATCTGAAACCGAGTATA'
SEQ_4 = 'AACATTTCGCGTCACGGGGGGCCTCTGAGAAGGACCCAACCTTAGAGGCAAACATCTCTATTCATTATGAGACCACTTCGCGACACTTGATCGACCTTACTACCACTGGCTACCTGGTGGCCATCAACGCATTTCAAAAGTCGATGAACGGGTTGGCAAGGGTCAGCATTGCCATCCTTTGACATCGCTCAGGGAAAGCGATGCAGTTTGGCGAAACCCTATATAAGGTACGTCGAAACACTTAATGAGAATGGTACGATGGTAGTATTCGTCAAGCAGTGGTAAGTACACGGTTATAGGCATGTGCCCAACCTTTTACTGGAATAATCGCGCGCTGCTCCCAACGAGGTAAAACGGGTTGTATGGTTTGCCATGCGAGTGGATATTCACCAGATTTTGCGGGTAGTAGACGGACAGCTTGCCAAAAGGCCTAGAGGGGGAATAGCAACACTACACACCTTCAGTCTATCGCCAAGAAACCATAATGCACCATTGTCGACCCGGGGCCGCGAGTAAACGGCAAACGACCGTTATTCGACGTCCCTGGTTCTCAGTGAGTAAAGGACCATCTTGGCGTCCTAGATATACAAACCATTTATGTGATTCTCGCCGTGCGGCCAACATGAGTGCTGAACTGCCTAGCCCCGATAGGAATAGTCAAAACACGTTACATACGCTCGCACGTAGGGAGGTGAAAGCGGGTAGGATTGGGTGGGACTCCCGTATGCCCGGAGGCAGTCGTCTTCCCGCAGACATCCACCAAGTCTGAAACGCTAGAGTCGGGCGAGATGTTACCTGTTAACTCACGTCTGGCTATATTGGGGCTGGCCATTTAAACAACGTAAATACTCTGTTTTTTATCACAAAAGTTGCAAAATTAGATTTGGCAAAGTGCTGAGCATGAGTTCGCTAATA'

def hamming_distance(s1: str, s2: str) -> int:
    """
    Calculates the hamming distance for two strings of equal length.

    :param s1:
    :param s2:
    :return:
    """

    distance = 0

    for item in zip(s1, s2):
        if item[0] != item[1]:
            distance += 1

    return distance

assert hamming_distance(SEQ_1, SEQ_2) == 7


print(hamming_distance(SEQ_3, SEQ_4))
