avaliacoesUsers = {'Ana': 
		{'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.5,
		 'Star Trek': 3.0, 
        'Star Wars': 3.0,
		 'Exterminador do Futuro': 3.5, 
		 'Norbit': 2.5},
	 
	  'Marcos': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 3.5, 
		 'Star Trek': 1.5, 
		 'Star Wars': 3.0,
        'Exterminador do Futuro': 5.0, 
		 'Norbit': 3.5}, 

	  'Pedro': 
	    {'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.0,
        'Star Wars': 4.0,
		 'Exterminador do Futuro': 3.5},
			 
	  'Claudia': 
		{'O Ultimato Bourne': 3.5, 
		 'Star Trek': 3.0,
		 'Star Wars': 4.5, 
		 'Exterminador do Futuro': 4.0, 
		 'Norbit': 2.5},
				 
	  'Adriano': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 4.0, 
		 'Star Trek': 2.0, 
        'Star Wars': 3.0,
        'Exterminador do Futuro': 3.0, 
		 'Norbit': 2.0}, 

	  'Janaina': 
	     {'Freddy x Jason': 3.0, 
	      'O Ultimato Bourne': 4.0,
	      'Star Wars': 3.0, 
	      'Exterminador do Futuro': 5.0, 
	      'Norbit': 3.5},
			  
	  'Leonardo': 
	    {'O Ultimato Bourne':4.5,
	     'Exterminador do Futuro':4.0,
         'Norbit':1.0}
}

avaliacoesModel = {'Model':{'Freddy x Jason', 
		 'O Ultimato Bourne',
		 'Star Trek',
		 'Star Wars',
        'Exterminador do Futuro', 
		 'Norbit'}
        }
  
avaliacoesMovies = {'Freddy x Jason': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Pedro': 2.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0 },
	 
	 'O Ultimato Bourne': 
		{'Ana': 3.5, 
		 'Marcos': 3.5,
		 'Pedro': 3.0, 
		 'Claudia': 3.5, 
		 'Adriano': 4.0, 
		 'Janaina': 4.0,
		 'Leonardo': 4.5 },
				 
	 'Star Trek': 
		{'Ana': 3.0, 
		 'Marcos:': 1.5,
		 'Claudia': 3.0, 
		 'Adriano': 2.0 },
	
	 'Exterminador do Futuro': 
		{'Ana': 3.5, 
		 'Marcos:': 5.0 ,
		 'Pedro': 3.5, 
		 'Claudia': 4.0, 
		 'Adriano': 3.0, 
		 'Janaina': 5.0,
		 'Leonardo': 4.0},
				 
	 'Norbit': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Claudia': 2.5, 
		 'Adriano': 2.0, 
		 'Janaina': 3.5,
		 'Leonardo': 1.0},
				 
	 'Star Wars': 
		{'Ana': 3.0, 
		 'Marcos:': 3.5,
		 'Pedro': 4.0, 
		 'Claudia': 4.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0}
}
        
##Fazer uma função de inserção de usuário
##Fazer um sistema que pergunta se o usuário existe 
##Excluir um usuário do sistema 
        
from math import sqrt

def knn(base,user1,user2):
    si = {}
    for item in base[user1]:
        if item in base[user2]: 
            si[item] = 1
        
    if len(si)==0: 
        return 0
        
    soma = sum([pow(base[user1][item] - base[user2][item], 2)
             for item in base[user1] if item in base[user2]])
    return 1/(1+sqrt(soma))

def getSim(base,user):
    sim = [(knn(base,user, users), users) 
                for users in base if users != user]
    sim.sort()
    sim.reverse()
    return sim [0:20]

def getRecomUser(base, user):
    totais = {}
    somaSim = {}
    for users in base:
        if users == user: continue
        sim = knn(base,user,users)

        if sim <= 0: continue
        
        for item in base[users]:
            if item not in base[user]:
                totais.setdefault (item, 0)
                totais[item]+= base[users][item]*sim
                somaSim.setdefault(item, 0)
                somaSim[item]+= sim
                
    rankings=[(total/somaSim[item], item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[0:20]   

def loadMovieLens(path='C:/ml-100k'):
    movies = {}
    for linha in open(path + '/u.item'):
        (id, titulo) = linha.split('|')[0:2]
        movies[id] = titulo
    
    base = {}
    for linha in open(path + '/u.data'):
        (user, idmovies,nota,tempo) = linha.split('\t')
        base.setdefault(user,{})
        base[user][movies[idmovies]] = float(nota)
    return base

def calItensSim(base):
    result = {}
    for item in base:
        notas = getSim(base, item)
        result[item] = notas
    return result

def getRecomItens(baseUser, simItens, user):
    notasUser = baseUser[user]
    notas={}
    totalSim={}
    #for(item , nota) in notasUser.item():
    for (item,nota) in notasUser.items():
        for(sim , item2) in simItens[item]:
            if item2 in notasUser: continue
            notas.setdefault(item2, 0)
            notas[item2] += sim * nota
            totalSim.setdefault(item2, 0)
            totalSim[item2] += sim
    rankings=[(score/totalSim[item],item) for item, score in notas.items()]
    rankings.sort()
    rankings.reverse()
    return rankings