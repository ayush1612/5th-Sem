function ChangeString(wrd)
{
   var nwrd = '';
   for(var i=0;i<wrd.length;i++)
   {
       if(wrd.charAt(i)>='a' && wrd.charAt(i)<='z')
       {
           if(wrd.charAt(i) != 'z')
            nwrd = nwrd + String.fromCharCode(wrd.charCodeAt(i) +1);
           else
            nwrd = nwrd + 'a';
       }
       else
        nwrd = nwrd + wrd.charAt(i);

   }

   //changing the vowels to capital letters
   for(var i = 0;i < wrd.length;i++)
   {
       var character = nwrd.charAt(i);

       if(character == 'a' || character == 'e' || character == 'i' || character == 'o' || character == 'u')
        nwrd = nwrd.slice(0,i) + character.toUpperCase() + nwrd.slice(i+1)
   }

   return nwrd;
}

console.log(ChangeString("hello*3"))