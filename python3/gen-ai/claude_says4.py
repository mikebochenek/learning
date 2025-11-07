# https://claude.ai/chat/5bceda00-c3c0-4de0-92b6-3d28e8b9a63b
# haiku 4.5 (not sonnet!)
# please show me a working python example which generates an image based on a short text.  
# using minimal models and open source libraries ONLY
# pip install diffusers transformers torch pillow

from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Use a lightweight model (768x768 max, good balance of speed and quality)
model_id = "runwayml/stable-diffusion-v1-5"

# Load the pipeline
print("Loading model... (this downloads ~4GB on first run)")
pipeline = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,  # Use half precision to save memory
    safety_checker=None  # Disable safety checker for speed
)

# Move to GPU if available, otherwise use CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
pipeline = pipeline.to(device)

# Enable memory optimization
pipeline.enable_attention_slicing()

# Generate image from text
prompt = "a serene landscape with mountains and a lake at sunset"
print(f"Generating image for: '{prompt}'")

with torch.no_grad():
    image = pipeline(
        prompt,
        height=512,
        width=512,
        num_inference_steps=30,  # Lower steps = faster but lower quality
        guidance_scale=7.5
    ).images[0]

# Save the image
image.save("generated_image.png")
print("Image saved as 'generated_image.png'")