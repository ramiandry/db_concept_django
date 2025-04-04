from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

@api_view(['POST'])
def chat(request):
    # Récupérer le message utilisateur depuis la requête
    user_message = request.data.get('message', '')

    # Vérifier si le message est vide
    if not user_message:
        return Response({"error": "Message is required"}, status=400)

    # Préparer la requête payload pour l'API Hugging Face
    payload = {
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ],
        "max_tokens": 500,
        "model": "deepseek-ai/DeepSeek-V3-0324-fast"
    }

    API_URL = "https://router.huggingface.co/nebius/v1/chat/completions"
    headers = {"Authorization": "Bearer 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"}

    try:
        # Envoyer la requête POST à l'API Hugging Face
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Vérifie si la requête a échoué
    except requests.exceptions.RequestException as e:
        # Gérer les erreurs de requête
        return Response({"error": str(e)}, status=500)

    # Récupérer la réponse JSON de Hugging Face
    response_data = response.json()

    # Vérifier si Hugging Face a retourné une réponse valide
    if "choices" in response_data and len(response_data["choices"]) > 0:
        # Retourner la réponse du modèle
        ai_message = response_data["choices"][0]["message"]
        return Response({"message": ai_message})
    else:
        return Response({"error": "No response from AI model"}, status=500)
