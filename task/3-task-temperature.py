from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

run(
    deployment_name='gpt-4o',
    print_only_content=True,
    temperature=0.7  # Controls randomness: 0.0 = deterministic, 2.0 = very creative
    # Try different values: 0.0, 0.5, 1.0, 1.5, 2.0
    # (Optional) Try temperature=2.1 to test validation
)