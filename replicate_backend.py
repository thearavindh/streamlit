import replicate
import os

def generate_video(prompt):
    try:
        replicate_api = os.environ.get("REPLICATE_API_TOKEN")
        replicate.Client(api_token=replicate_api)

        output = replicate.run(
            "cjwbw/animatediff:fb9c1cbd8d22b17913bb682d3e3c3d8ee3342197f8f72b44f58c34e62b6f8c51",
            input={
                "prompt": prompt,
                "num_frames": 16,
                "width": 512,
                "height": 512,
                "guidance_scale": 7.5,
                "num_inference_steps": 25
            }
        )
        return output if output else None
    except Exception as e:
        print("Error generating video:", e)
        return None
