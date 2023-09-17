
import os
from content_curation import ContentCurator
from seo_optimization import SEO_Optimizer
from user_interaction import UserInteractor
from publishing_automation import Publisher
from content_review import ContentReviewer

def main():
    # Load configurations
    with open(os.path.join("..", "config", "wordpress_api_config.json")) as config_file:
        config = json.load(config_file)

    # Initialize modules
    curator = ContentCurator(config)
    seo_optimizer = SEO_Optimizer(config)
    user_interactor = UserInteractor(config)
    publisher = Publisher(config)
    reviewer = ContentReviewer(config)

    # Curate content
    curated_content = curator.curate_content()

    # Optimize content for SEO
    seo_optimized_content = seo_optimizer.optimize(curated_content)

    # Interact with users
    user_interactor.interact()

    # Automate publishing
    publisher.publish(seo_optimized_content)

    # Review and edit AI-generated content
    reviewer.review()

if __name__ == "__main__":
    main()
