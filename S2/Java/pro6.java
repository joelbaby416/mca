public class pro6{
    public static void main(String []args){
        String temp;
        int i,j;
        String str[] = new String[5];
        str[0] = "apple";
        str[1] = "mango";
        str[2] = "avacado";
        str[3] = "kiwi";
        str[4] = "cherry";
         System.out.println("The strings before sorting:");
        for(i=0;i<5;i++)
         {
             System.out.println(str[i]);
         }
        
        for (i=0; i<5; i++)
          {
              for(j=i+1;j<5;j++)
                {
                    if((str[i].compareTo(str[j]))>0)
                      {
                          temp=str[i];
                          str[i]=str[j];
                          str[j]=temp;
                      }
                }
              
          }
        System.out.println("\nThe strings after sorting:");
        for(i=0;i<5;i++)
         {
             System.out.println(str[i]);
         }
    }
}
