# Bee-API
Bee API is a FastAPI-based backend application developed specifically to improve the quality of Education using Personalized Learning Methodologies.

## Run the below command to setup
`pip install -r requirements.txt`

### Endpoints:
**/**: for status 200 basic Health Check API
**/questions**: accepts var Topic:str and returns a series of questions with varing difficulty
**/questions/subtopics**: accepts var Topic:str and difficulty:str and returns a series of Sub-Topics to focus based on analysis.