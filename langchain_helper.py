from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

#sequential chain

llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    #chain1 : 레스토랑 이름 지어주기 체인
    Prompt_tempate_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I WANNA OPEN A RESTAURENT FOR {cuisine} FOOD. SUGGEST A FENCY NAME FOR THEIS."
    )
    name_chain = LLMChain(llm=llm, prompt=Prompt_tempate_name, output_key="restaurant_name")
    #chain2 : 메뉴 만들어주기 체인
    Prompt_tempate_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="SUGGEST SOME MENU ITEMS FOR {restaurant_name}."
    )
    Food_items_chain = LLMChain(llm=llm, prompt=Prompt_tempate_items, output_key="menu_items")
    # 결과로 나오 메뉴들 menu_item이라는 키로~
    chain = SequentialChain(
        chains=[name_chain, Food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )
    #우리는 이렇게 나온 결과를 응답으로 반환함
    response = chain({'cuisine': cuisine})

    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items(("KOREAN")))








