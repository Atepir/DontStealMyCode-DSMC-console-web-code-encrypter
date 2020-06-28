{- 
 - 1. Listes polymorphes 
 - - 1. 
-}

nth n lst = case lst of 
{
	[] -> error "Liste vide";
	t:r -> if n==0 then t else nth (n-1) r
}

rev lst = case lst of 
{
	[] -> [];
	t:r -> (rev r)++[t]
}

sans_doublons lst = case lst of
{
	[] -> [];
	[x] -> [x];
	t:q:r -> let p = sans_doublons (q:r) in 
		if t==q then p else t:p
}

pack lst = case lst of
{
	[] -> [];
	[x] -> [[x]];
	x:y:r -> let p = pack (y:r) in 
		if x==y then (case p of
				{
					t:r -> (x:t):r;
					_ -> error "pack"
				})	
		else [x]:p
}

{- Carte Couleur -}

data Couleur = 
        Coeur
      | Carreau
      | Pique
      | Trefle deriving Eq

data Cartes =
	As Couleur
      | Roi Couleur
      | Dame Couleur
      | Valet Couleur
      | Petite Integer Couleur

couleur_of_carte ca = case ca of
{
 As a -> a;
 Roi a -> a;
 Dame a -> a;
 Valet a -> a;
 Petite _ a -> a;
}
meme_couleur c1 c2 = 
	if couleur_of_carte c1 == couleur_of_carte c2 then True
	else False

force ca = case ca of
{
 As a -> 14;
 Roi a -> 13;
 Dame a -> 12;
 Valet a -> 11;
 Petite a _ -> a;
}

moins_forte c1 c2 =
	if force c1 < force c2 then True
	else False
