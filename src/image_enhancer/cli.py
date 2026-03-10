import argparse 
from image_enhancer.pipeline_executor import PipelineExecutor

def main():
    parser = argparse.ArgumentParser(
                        prog='Config Runner',
                        description='This will run various image operations',
                        epilog='Image enhancement engine')

    parser.add_argument('config_path',
                        metavar ='N',
                        type = str,
                        help ='Path to JSON config file')

    # this parses the config path
    args = parser.parse_args()

    # instantiating the executor
    pipe_executor = PipelineExecutor(args.config_path)

    pipe_executor.run()
    

if __name__ == "__main__":
    main()