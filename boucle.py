# Nombre d'abonnés (2500)

subscribers_count = 2500

#10% d'audience par mois

months = 0

# Combien d'abonnés aura-t-il après 2 ans ? (24 mois)

while months <= 24:

# Augmenter l'audience

    subscribers_count *= 1.10
    
    # Afficher le nombre d'abonnés
    
    print("Vous avez actuellement {} abonnés !".format (subscribers_count))
    
    #On passe au mois suivant
    
    months += 1
