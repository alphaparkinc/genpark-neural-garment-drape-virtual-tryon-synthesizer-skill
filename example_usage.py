from client import NeuralGarmentDrapeVirtualTryonSynthesizerClient

def main():
    client = NeuralGarmentDrapeVirtualTryonSynthesizerClient()
    res = client.synthesize_virtual_tryon('MALE_SLIM_FIT_L', 'https://assets.genpark.ai/garments/tailored_blazer.png')
    print('Try-On Job: ' + res['tryon_job_id'] + ' | ' + res['body_model'])
    print('Physics: ' + res['fabric_physics_model'] + ' (Crease Accuracy: ' + str(res['wrinkle_micro_crease_accuracy_pct']) + '%)')
    print('Resolution: ' + res['render_resolution'] + ' | Pass: ' + str(res['occlusion_edge_blending_passed']))
    print('Result URL: ' + res['photorealistic_render_url'])

if __name__ == '__main__':
    main()
