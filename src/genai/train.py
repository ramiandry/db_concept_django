def train(question): 
    training = f"""
# 1. Si la question est de type demande de MCD / Merise / conception de base de données / modélisation de données

question : je veux un MCD de gestion de produits

réponse :
{{
    "type": "mcd",
    "response": {{
        "defaultNodes": [
            {{
                "id": "1",
                "position": {{ "x": 0, "y": 0 }},
                "type": "databaseSchema",
                "data": {{
                    "label": "Products",
                    "schema": [
                        {{ "title": "id", "type": "uuid" }},
                        {{ "title": "name", "type": "varchar" }},
                        {{ "title": "description", "type": "varchar" }},
                        {{ "title": "warehouse_id", "type": "uuid" }},
                        {{ "title": "supplier_id", "type": "uuid" }},
                        {{ "title": "price", "type": "money" }},
                        {{ "title": "quantity", "type": "int4" }}
                    ]
                }}
            }},
            {{
                "id": "2",
                "position": {{ "x": 350, "y": -100 }},
                "type": "databaseSchema",
                "data": {{
                    "label": "Warehouses",
                    "schema": [
                        {{ "title": "id", "type": "uuid" }},
                        {{ "title": "name", "type": "varchar" }},
                        {{ "title": "address", "type": "varchar" }},
                        {{ "title": "capacity", "type": "int4" }}
                    ]
                }}
            }},
            {{
                "id": "3",
                "position": {{ "x": 350, "y": 200 }},
                "type": "databaseSchema",
                "data": {{
                    "label": "Suppliers",
                    "schema": [
                        {{ "title": "id", "type": "uuid" }},
                        {{ "title": "name", "type": "varchar" }},
                        {{ "title": "description", "type": "varchar" }},
                        {{ "title": "country", "type": "varchar" }}
                    ]
                }}
            }}
        ],
        "defaultEdges": [
            {{
                "id": "products-warehouses",
                "source": "1",
                "target": "2",
                "sourceHandle": "warehouse_id",
                "targetHandle": "id"
            }},
            {{
                "id": "products-suppliers",
                "source": "1",
                "target": "3",
                "sourceHandle": "supplier_id",
                "targetHandle": "id"
            }}
        ]
    }}
}}

# 2. Si la question est de type texte ou question ouverte

question : je veux une description de la gestion de produits

réponse :
{{
    "type": "text",
    "response": "La gestion de produits est un processus qui implique la planification, le développement, la commercialisation et la vente de produits. Cela comprend la gestion des stocks, la gestion des fournisseurs, la gestion des prix et la gestion des ventes. La gestion de produits vise à maximiser les profits tout en répondant aux besoins des clients. Elle nécessite une compréhension approfondie du marché, des tendances et des comportements des consommateurs. La gestion de produits est essentielle pour assurer le succès d'une entreprise sur le long terme."
}}

Voici la question : {question}
"""
    return training
