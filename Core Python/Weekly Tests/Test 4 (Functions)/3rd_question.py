'''
WAP to print following patterns :

 *   *   *   *   *   *   *   *  
                         *      
                     *          
                 *              
             *                  
         *                      
     *                          
 *   *   *   *   *   *   *   * 

 '''
for i in range(1,9):
    for j in range(1,9):
        if(i==1 or i==8):
            print(" * ", end = " ")
        elif (j == 9-i):
            print(" * ", end = " ")
        else:
            print("   ", end = " ")
    print()