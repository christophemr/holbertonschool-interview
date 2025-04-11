#include <stdlib.h>
#include <string.h>

int *find_substring(char const *s, char const **words, int nb_words, int *n) {
    size_t word_len = strlen(words[0]);
    size_t total_len = nb_words * word_len;
    size_t s_len = strlen(s);
    int *indices = malloc((s_len - total_len + 1) * sizeof(int));
    int indices_count = 0;

    if (s == NULL || words == NULL || nb_words == 0 || word_len == 0) {
        *n = 0;
        return NULL;
    }

    for (size_t i = 0; i <= s_len - total_len; i++) {
        int *word_used = calloc(nb_words, sizeof(int));
        size_t j;

        for (j = 0; j < (size_t)nb_words; j++) {
            int found = 0;
            for (int k = 0; k < nb_words; k++) {
                if (!word_used[k] && strncmp(&s[i + j * word_len], words[k], word_len) == 0) {
                    word_used[k] = 1;
                    found = 1;
                    break;
                }
            }
            if (!found) break;
        }

        if (j == (size_t)nb_words) {
            indices[indices_count++] = (int)i;
        }

        free(word_used);
    }

    if (indices_count == 0) {
        free(indices);
        *n = 0;
        return NULL;
    }

    *n = indices_count;
    return indices;
}
