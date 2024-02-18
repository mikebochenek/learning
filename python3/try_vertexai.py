import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

def generate():
  vertexai.init(project="smarty-414711", location="us-central1")
  model = GenerativeModel("gemini-pro")
  responses = model.generate_content(
    """Read the below multiple choice question carefully, and provide the best answer:

	Git. You are working on a clean Git install with no special configurations. While on the main branch, you create a new branch called mybranch, check it out, and commit data to it. Then, you check out the main branch and give the command git merge mybranch. What is the outcome of this operation?
	(a) A rebase, creating conflicts during the merge
	(b) A fast-forward merge, where main tip is moved to mybranch tip
	(c) A three-way merge, where main is deleted after being merged with mybranch
	(d) A failure because main and mybranch contain different commits""",
    generation_config={
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1
    },
    safety_settings={
          generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
    stream=True,
  )
  
  for response in responses:
    print(response.text, end="")


generate()