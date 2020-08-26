print("    *", sep = ' ', end = '\n')
print("   * *", sep = ' ', end = '\n')
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****\n")


tree = '''    
              *
             * *
            *   *
           *     *
          ***   ***
            *   *
            *   *
            *****
            '''
print(f'{tree}'* 2)

print('    *\t\t' * 2 ,'   * * \t\t' * 2, '  *   * \t' * 2, ' *     * \t' * 2, '***   *** \t' * 2, '  *   * \t' * 2, '  *   * \t' * 2, '  ***** \t' * 2, sep = '\n', end = '\n')