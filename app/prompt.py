# Example RetrievalQAWithSources chain prompt override.

from langchain.prompts import PromptTemplate

question_prompt_template = """Use the following portion of a long document to see if any of the text is relevant to answer the question. 
Return any relevant text verbatim.
{context}
Question: {question}
Relevant text, if any:"""
QUESTION_PROMPT = PromptTemplate(
    template=question_prompt_template, input_variables=["context", "question"]
)

combine_prompt_template = """Please act as a Financial Analyst of a company and pay attention to the financial statements in the given document. Given the following extracted parts of a long document and a question, create a final answer with references ("SOURCES"). If you don't know the answer, just say that you don't know. Don't try to make up an answer. ALWAYS return a "SOURCES" part in your answer in the following format: "sources: <source 1>, <source 2>" etc. Remember that Operating Income = Revenue - Operating Expenses for a company. To calculate the operating margin, you divide operating income by revenue.

QUESTION: What is the operating margin?
=========
Content: Three Months Ended
Six Months Ended
July 30, April 30, July 31, July 30, July 31,
2023 2023 2022 2023 2022
GAAP gross profit $ 9,462 $ 4,648 $ 2,915 $ 14,110 $ 8,346
GAAP gross margin 70.1% 64.6% 43.5% 68.2% 55.7%
Acquisition-related and other costs (A) 119 119 121 239 214
Stock-based compensation expense (B) 31 27 38 58 76
IP-related costs 2 8 — 10 —
Non-GAAP gross profit $ 9,614 $ 4,802 $ 3,074 $ 14,417 $ 8,636
Non-GAAP gross margin 71.2% 66.8% 45.9% 69.7% 57.6%
GAAP operating expenses $ 2,662 $ 2,508 $ 2,416 $ 5,169 $ 5,979
Stock-based compensation expense (B) (811) (708) (611) (1,518) (1,151)
Acquisition-related and other costs (A) (18) (54) (54) (72) (110)
Acquisition termination cost — — — — (1,353)
Legal settlement costs — — — — (7)
Contributions — — (2) — (2)
Other (C) 5 4 — 10 —
Non-GAAP operating expenses $ 1,838 $ 1,750 $ 1,749 $ 3,589 $ 3,356
GAAP operating income $ 6,800 $ 2,140 $ 499 $ 8,941 $ 2,367
Total impact of non-GAAP adjustments to
operating income 976 912 826 1,887 2,913
Non-GAAP operating income $ 7,776 $ 3,052 $ 1,325 $ 10,828 $ 5,280
GAAP other income (expense), net $ 181 $ 69 $ (24) $ 249 $ (87)
(Gains) losses from non-affiliated
investments
(62) 14 7 (46) 24
Interest expense related to amortization of
debt discount 1 1 1 2 2
Non-GAAP other income (expense), net $ 120 $ 84 $ (16) $ 205 $ (61)
GAAP net income $ 6,188 $ 2,043 $ 656 $ 8,232 $ 2,274
Total pre-tax impact of non-GAAP
adjustments 915 927 833 1,843 2,940
Income tax impact of non-GAAP
adjustments (D) (363) (257) (197) (622) (478)
Non-GAAP net income $ 6,740 $ 2,713 $ 1,292 $ 9,453 $ 4,736
Source: source_8

Content: Outlook
($ in millions)
GAAP gross margin 71.5%
Impact of stock-based compensation expense, acquisition-related costs, and other costs 1.0%
Non-GAAP gross margin 72.5%
GAAP operating expenses $ 2,950
Stock-based compensation expense, acquisition-related costs, and other costs (950)
Non-GAAP operating expenses $ 2,000
About NVIDIA
Since its founding in 1993, NVIDIA (NASDAQ: NVDA) has been a pioneer in accelerated computing. The company’s
invention of the GPU in 1999 sparked the growth of the PC gaming market, redefined computer graphics, ignited the era of
modern AI and is fueling industrial digitalization across markets. NVIDIA is now a full-stack computing company with data-
center-scale offerings that are reshaping industry. More information at https://nvidianews.nvidia.com/.
Certain statements in this press release including, but not limited to, statements as to: companies worldwide transitioning
from general-purpose to accelerated computing and generative AI; NVIDIA GPUs running CUDA AI software stack making
up the computing infrastructure of generative AI; the race to adopt generative AI; NVIDIA’s plans to continue share
repurchases; NVIDIA’s next quarterly cash dividend; NVIDIA’s financial outlook and expected tax rates for the third quarter of
fiscal 2024; the benefits, impact, performance, features and availability of our products and technologies, including the
NVIDIA GH200 Grace Hopper Superchip, NVIDIA L40S GPU, NVIDIA OVX, NVIDIA AI Enterprise, BlueField DPUs, NVIDIA
MGX, NVIDIA Omniverse, NVIDIA Spectrum-X, NVIDIA RTX workstations, NVIDIA RTX 6000 Ada GPU, NVIDIA Omniverse
Enterprise software, NVIDIA H100 Tensor Core GPU, NVIDIA DGX Cloud AI, NVIDIA AI Workbench, NVIDIA AI Enterprise
4.0, the GeForce RTX 4060 family, NVIDIA Ada Lovelace, DLSS, NVIDIA Avatar Cloud Engine, NVIDIA’s RTX Remix,
NVIDIA RTX 5000, RTX 4500 and RTX 4000, and NVIDIA DRIVE Orin; and the benefits and impact of NVIDIA’s
partnerships with ServiceNow, Accenture, VMware, Snowflake, WPP, SoftBank, Hugging Face, and MediaTek, and
NVIDIA’s Alliance for OpenUSD with Pixar, Adobe, Apple and Autodesk are forward-looking statements that are subject to
risks and uncertainties that could cause results to be materially different than expectations. Important factors that could cause
actual results to differ materially include: global economic conditions; our reliance on third parties to manufacture, assemble,
package and test our products; the impact of technological development and competition; development of new products and
technologies or enhancements to our existing product and technologies; market acceptance of our products or our partners’
products; design, manufacturing or software defects; changes in consumer preferences or demands; changes in industry
standards and interfaces; unexpected loss of performance of our products or technologies when integrated into systems; as
Source: source_10

Content: different from non-GAAP measures used by other companies.
NVIDIA CORPORATION
CONDENSED CONSOLIDATED STATEMENTS OF INCOME
(In millions, except per share data)
(Unaudited)
Three Months Ended Six Months Ended
July 30, July 31, July 30, July 31,
2023 2022 2023 2022
Revenue $ 13,507 $ 6,704 $ 20,699 $ 14,992
Cost of revenue 4,045 3,789 6,589 6,646
Gross profit 9,462 2,915 14,110 8,346
Operating expenses
Research and development 2,040 1,824 3,916 3,443
Sales, general and administrative 622 592 1,253 1,183
Acquisition termination cost — — — 1,353
Total operating expenses 2,662 2,416 5,169 5,979
Source: source_4

Content: Operating income 6,800 499 8,941 2,367
Interest income 187 46 338 64
Interest expense (65) (65) (131) (132)
Other, net 59 (5) 42 (19)
Other income (expense), net 181 (24) 249 (87)
Income before income tax 6,981 475 9,190 2,280
Income tax expense (benefit) 793 (181) 958 6
Net income $ 6,188 $ 656 $ 8,232 $ 2,274
Net income per share:
Basic $ 2.50 $ 0.26 $ 3.33 $ 0.91
Diluted $ 2.48 $ 0.26 $ 3.30 $ 0.90
Weighted average shares used in per share computation:
Basic 2,473 2,495 2,472 2,500
Diluted 2,499 2,516 2,495 2,526
NVIDIA CORPORATION
CONDENSED CONSOLIDATED BALANCE SHEETS
(In millions)
(Unaudited)
July 30, 2023 January 29, 2023
ASSETS
Current assets:
Cash, cash equivalents and marketable securities $ 16,023 $ 13,296
Accounts receivable, net 7,066 3,827
Inventories 4,319 5,159
Prepaid expenses and other current assets 1,389 791
Total current assets 28,797 23,073
Property and equipment, net 3,799 3,807
Operating lease assets 1,235 1,038
Goodwill 4,430 4,372
Intangible assets, net 1,395 1,676
Deferred income tax assets
5,398 3,396
Other assets 4,501 3,820
Total assets $ 49,555 $ 41,182
LIABILITIES AND SHAREHOLDERS' EQUITY
Source: source_5
=========
FINAL ANSWER:

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""
COMBINE_PROMPT = PromptTemplate(
    template=combine_prompt_template, input_variables=["summaries", "question"]
)

EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)
