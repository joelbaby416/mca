public class pro8 {
	     public static void main(String []args){
	        String text = "Joel Baby";
	        System.out.println("Original Text: "+text);
	        System.out.println("\nGiven text is empty: "+text.isEmpty());
	        System.out.println("\nLength of text: "+text.length());
	        System.out.println("\nUpper Case: "+text.toUpperCase());
	        System.out.println("\nLower Case: "+text.toLowerCase());
	        System.out.println("\nReplace: "+text.replaceAll(text, "Alex"));
	        System.out.println("\nReplace first word: "+text.replaceFirst("Joel","Albert"));
	        System.out.println("\nReplace O with $: "+text.replace('J','$'));
	        System.out.println("\nConcatenation with: "+text.concat(" ").concat("M"));
	     }
	}
