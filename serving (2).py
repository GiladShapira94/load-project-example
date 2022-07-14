import numpy as np
import mlrun
import os
from cloudpickle import load
from mlrun.artifacts import get_artifact_meta
class LGBMModel(mlrun.serving.V2ModelServer):
    
    def load(self):
        model_file, extra_data = self.get_model('.pkl')
        self.model_meta = get_artifact_meta(self.model_path)[0]
        self.model = load(open(model_file, 'rb'))

    def predict(self, body):
        try:
#             print("model_hash",self.model_meta.hash)
            feats = np.asarray(body['inputs'])
            result = self.model.predict(feats)
            response = [result.tolist(),f"Model Hash {self.model_meta.hash}"]
            return response
        except Exception as e:
            raise Exception("Failed to predict %s" % e)