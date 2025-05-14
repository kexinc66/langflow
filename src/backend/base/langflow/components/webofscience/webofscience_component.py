from langflow.interface.custom_components import CustomComponent

class WebOfScienceSearchComponent(CustomComponent):
    display_name = "Web of Science Search"
    description = "Mock component to simulate search from Web of Science"
    
    def build_config(self):
        return {
            "keywords": {"display_name": "Search Keywords"},
            "start_year": {"display_name": "Start Year"},
            "end_year": {"display_name": "End Year"}
        }

    def build(self, keywords: str, start_year: str = "2015", end_year: str = "2025") -> list:
        mock_result = [
            {
                "title": "Sample WoS Paper Title",
                "authors": "Smith J., Doe A.",
                "abstract": "This is a mock abstract from WoS.",
                "link": "https://www.webofscience.com/sample-link",
                "source": "Web of Science"
            },
            {
                "title": "Another Mock Article",
                "authors": "Lee C., Wang B.",
                "abstract": "Another abstract from the WoS dataset.",
                "link": "https://www.webofscience.com/sample-link-2",
                "source": "Web of Science"
            }
        ]
        return mock_result

