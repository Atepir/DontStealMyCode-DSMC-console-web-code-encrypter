somme_filtre n f = 

   if n==0 then 0 

           else (somme_filtre (n-1) f)+(if f n then n else 0)
