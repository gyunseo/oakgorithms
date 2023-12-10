#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include "avl.h"

bool search(Node *p_node, int data)
{
    if (p_node == NULL)
        return false;
    if (p_node->data == data)
        return true;
    if (data < p_node->data)
        return search(p_node->left_child, data);
    if (data > p_node->data)
        return search(p_node->right_child, data);
}

int main()
{

    int random[MAX_VAL] = {935, 378, 438, 515, 312, 31, 680, 857, 141, 853, 420, 906, 357, 555, 295, 781, 246, 424, 831, 110, 338, 537, 496, 134, 399, 289, 987, 307, 504, 858, 396, 418, 895, 602, 77, 445, 64, 845, 812, 873, 18, 889, 314, 395, 605, 535, 549, 437, 302, 488, 185, 953, 655, 370, 575, 355, 348, 166, 236, 848, 352, 460, 683, 955, 977, 739, 106, 568, 214, 728, 844, 419, 799, 647, 232, 431, 495, 416, 570, 651, 741, 721, 984, 239, 207, 709, 523, 299, 398, 14, 598, 707, 835, 805, 644, 30, 36, 865, 333, 536, 978, 305, 216, 628, 326, 990, 769, 947, 254, 365, 382, 809, 670, 757, 894, 205, 29, 929, 701, 803, 168, 966, 108, 852, 228, 643, 459, 117, 135, 846, 625, 126, 75, 818, 922, 696, 179, 669, 190, 38, 461, 609, 19, 82, 745, 13, 914, 633, 293, 726, 698, 556, 464, 84, 442, 833, 883, 798, 429, 509, 893, 162, 874, 942, 470, 145, 130, 21, 611, 640, 712, 939, 175, 975, 6, 629, 650, 182, 787, 264, 816, 172, 60, 770, 675, 262, 155, 630, 259, 391, 898, 426, 294, 795, 212, 779, 838, 917, 358, 573, 664, 300, 183, 563, 298, 649, 170, 776, 158, 436, 646, 337, 538, 247, 95, 807, 909, 706, 915, 90, 943, 999, 581, 336, 740, 639, 577, 58, 231, 198, 296, 189, 451, 755, 635, 483, 560, 994, 235, 751, 667, 327, 397, 364, 8, 72, 322, 908, 674, 161, 174, 484, 241, 855, 375, 404, 73, 403, 794, 320, 743, 368, 614, 584, 292, 279, 897, 610, 903, 491, 202, 88, 780, 710, 457, 754, 466, 7, 606, 956, 641, 736, 53, 277, 784, 92, 177, 654, 829, 271, 423, 518, 136, 522, 306, 427, 384, 220, 221, 169, 4, 383, 827, 219, 720, 359, 713, 493, 160, 626, 516, 363, 600, 912, 923, 882, 961, 193, 371, 272, 65, 876, 5, 854, 267, 103, 32, 525, 725, 346, 186, 361, 422, 280, 767, 982, 590, 948, 937, 824, 730, 719, 409, 389, 249, 676, 552, 335, 128, 951, 268, 450, 532, 534, 329, 0, 594, 26, 208, 204, 502, 245, 660, 350, 54, 813, 604, 123, 621, 481, 946, 482, 913, 603, 456, 83, 967, 840, 107, 224, 301, 932, 261, 711, 94, 201, 574, 561, 806, 634, 708, 662, 27, 941, 585, 132, 954, 275, 774, 478, 665, 229, 979, 860, 679, 925, 138, 324, 480, 924, 252, 528, 133, 321, 435, 390, 34, 197, 447, 637, 362, 933, 759, 181, 225, 227, 533, 125, 820, 940, 930, 785, 46, 868, 756, 686, 251, 152, 304, 332, 586, 661, 323, 55, 777, 750, 171, 116, 511, 102, 519, 191, 682, 297, 526, 722, 433, 454, 163, 52, 131, 508, 700, 288, 583, 960, 789, 543, 931, 620, 319, 869, 41, 612, 645, 226, 39, 666, 764, 127, 167, 911, 449, 192, 514, 360, 989, 47, 825, 652, 79, 862, 849, 503, 156, 788, 808, 916, 851, 425, 693, 810, 732, 811, 265, 473, 340, 353, 957, 501, 237, 291, 256, 417, 387, 165, 487, 248, 507, 513, 520, 737, 448, 379, 114, 199, 105, 101, 920, 672, 642, 613, 768, 995, 928, 616, 121, 74, 593, 492, 303, 196, 659, 510, 993, 339, 823, 143, 184, 485, 443, 444, 981, 949, 945, 821, 122, 678, 223, 744, 576, 775, 40, 636, 580, 542, 401, 334, 692, 996, 270, 206, 673, 622, 469, 521, 412, 258, 689, 325, 638, 120, 310, 234, 386, 439, 499, 729, 677, 233, 668, 255, 896, 627, 104, 311, 551, 554, 150, 548, 356, 468, 253, 564, 632, 907, 178, 287, 62, 476, 691, 773, 290, 331, 3, 385, 421, 273, 944, 342, 494, 624, 658, 685, 572, 527, 815, 15, 173, 631, 124, 369, 276, 936, 618, 20, 657, 550, 814, 23, 512, 144, 147, 702, 763, 111, 847, 81, 37, 154, 453, 547, 731, 98, 599, 716, 983, 345, 567, 432, 866, 880, 919, 366, 148, 187, 388, 33, 531, 529, 828, 479, 900, 842, 965, 238, 733, 796, 440, 410, 49, 997, 699, 748, 579, 91, 374, 392, 316, 477, 991, 51, 59, 988, 875, 772, 215, 500, 562, 411, 109, 164, 260, 653, 742, 471, 57, 217, 684, 274, 752, 203, 430, 890, 2, 44, 826, 569, 142, 557, 68, 973, 864, 974, 12, 463, 180, 969, 926, 462, 129, 22, 778, 565, 498, 588, 839, 910, 714, 671, 886, 596, 140, 28, 863, 524, 856, 766, 746, 100, 283, 112, 793, 455, 980, 608, 282, 834, 372, 506, 541, 553, 377, 952, 308, 892, 56, 465, 985, 250, 349, 717, 704, 623, 48, 45, 832, 539, 475, 582, 800, 986, 24, 9, 373, 63, 472, 99, 963, 972, 753, 927, 901, 242, 578, 734, 934, 341, 601, 408, 87, 688, 86, 269, 16, 607, 747, 446, 137, 78, 151, 904, 783, 802, 615, 35, 381, 888, 765, 71, 843, 921, 394, 958, 405, 592, 315, 705, 619, 782, 97, 497, 530, 505, 343, 715, 559, 801, 458, 517, 690, 905, 591, 486, 309, 263, 822, 902, 962, 918, 749, 317, 70, 881, 792, 467, 407, 428, 347, 209, 210, 434, 400, 546, 66, 850, 819, 976, 119, 257, 571, 113, 797, 1, 176, 149, 25, 380, 240, 146, 992, 222, 313, 11, 950, 791, 718, 695, 413, 762, 998, 328, 761, 50, 159, 17, 703, 724, 211, 230, 93, 69, 354, 879, 887, 867, 959, 85, 971, 42, 617, 697, 115, 694, 318, 76, 687, 96, 597, 415, 139, 663, 871, 544, 351, 681, 67, 899, 281, 877, 804, 278, 970, 968, 870, 376, 266, 727, 723, 452, 891, 61, 474, 964, 656, 738, 786, 836, 490, 566, 837, 884, 195, 441, 43, 545, 771, 200, 244, 80, 213, 859, 830, 595, 872, 367, 218, 284, 285, 817, 188, 406, 153, 414, 243, 587, 344, 861, 558, 885, 402, 330, 89, 735, 489, 758, 540, 790, 648, 393, 286, 938, 841, 10, 760, 157, 589, 878, 194, 118};
    time_t start, end;
    for (int i = 0; i < MAX_VAL; i++)
    {
        root = insert_node(root, random[i]);
    }
    print_AVL_tree(root, 0);
    printf("\n");
    start = clock();
    bool found_flag = search(root, 438);
    end = clock();
    printf("avl tree search time: %.10f\n", (double)(end - start) / CLOCKS_PER_SEC);
    if (found_flag)
        printf("avl tree item searched!\n");
    // unmount nodes
    while (root)
        root = delete_node(root, root->data);
    root = insert_node(root, 5);
    root = insert_node(root, 3);
    root = insert_node(root, 10);
    root = insert_node(root, 2);
    root = insert_node(root, 4);
    root = insert_node(root, 7);
    root = insert_node(root, 11);
    root = insert_node(root, 1);
    root = insert_node(root, 6);
    root = insert_node(root, 9);
    root = insert_node(root, 12);
    root = insert_node(root, 8);
    print_AVL_tree(root, 0);
    printf("\n");

    start = clock();
    root = delete_node(root, 5);
    end = clock();
    printf("avl tree delete time: %.10f\n", (double)(end - start) / CLOCKS_PER_SEC);
    return 0;
}
