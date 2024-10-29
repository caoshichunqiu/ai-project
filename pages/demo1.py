'''
制作一个带有自定义角色大模型应用
1.大模型对象
2.提示词对象
3，链chain。
使用流程：首先，构建一个大模型对象，然后创建提示词工程对象，然后使用langchain中的chain链将大模型对象和提示词工程对象组合起来，
此时回答问题使用链来回答
基于历史聊天记录的对话模型
1.大模型对象
2.提示词工程对象
3
'''

#解决聊天界面不能渲染以往旧对话的信息
#streamlit每次输入框发送完成数据后，页面都会重新加载
import streamlit as st

#langchain调用大模型，导入langchain的代码，大模型对象
#引入一个提示词对象，langchain中有很多提示词对象，只用一个简单的对象PromptTemplate
from langchain.prompts import PromptTemplate
#引入一个langchain的链对象，简单链LLMChain
from langchain.chains import LLMChain

from langchain_openai import ChatOpenAI
#引入一个基于内存的记忆模块对象
from langchain.memory import ConversationBufferMemory



#构建一个大模型-智谱ai
model=ChatOpenAI(
    temperature=0.8,#温度，此处理解为ai回答内容的创新性，越接近1越创新
    model="glm-4-plus",#大模型的名字
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="b9555c1df61e441435592b83c044a4e2.qgHyKediqm4A078v"
)
#创建记忆模块对象,记忆模块需要结合提示词模块来使用，记忆模块保存的数据当作提示词信息传递给大模型
if"memory" not in st.session_state:
    st.session_state.memory=ConversationBufferMemory(memory_key="history")
#创建提示词对象
prompt = PromptTemplate.from_template("你的名字叫坤坤，你现在扮演一个逆子，性格幽默风趣的，你现在要和你的爸爸对话，"
                             "你只需要回应你爸说的话，其余的话不要输出，你爸爸说的话是{input}，你和你爸爸的历史对话为{history}")
#使用langchain链关联大模型提示词对象
chain=LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memory,
)
st.title('凡爹，我是你儿子坤坤')
#构建一个缓存，用来保存聊天记录
if"cache" not in st.session_state:
    st.session_state.cache = []
else:
    #需要从缓存中获取对话信息，在界面中渲染，缓存两块内容，角色，角色的消息
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])

#创建一个聊天输入框
problem=st.chat_input("父亲大人有什么吩咐")
if problem:
    #1.将用户的问题输入到界面上
    with st.chat_message("user"):
        st.write(problem)
    #将用户的问题添加到缓存
    st.session_state.cache.append({"role": "user", "content": problem})
    #2.调用链对象回答问题
    result=chain.invoke({"input": problem})
    #result=model.invoke(problem)
    #3.将大模型回答的问题输出到界面上
    with st.chat_message("assistant"):
        st.write(result['text'])
    st.session_state.cache.append({"role": "user", "content": result['text']})