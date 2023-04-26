#!/usr/bin/env python
# coding: utf-8

# **Load the required data and dataset**

# In[1]:


# Load the required datasets 
import pandas as pd 
import panel as pn
import hvplot.pandas
import holoviews as hv
import numpy as np
import seaborn as sns 
import ast
import warnings

warnings.filterwarnings("ignore")

hv.extension('bokeh')

pn.extension(sizing_mode="stretch_width")


# Load the relevant data
portfolio = pd.read_csv("data/output/portfolio_clean.csv")
profile = pd.read_csv("data/output/profile_clean.csv")
transcript = pd.read_csv("data/output/transcript_clean.csv")

# Create new age groups 
bins= [18,36,56,76,150]
labels = ['Youth','Middle-Aged','Retired','Aging']

profile['ageGroup'] = pd.cut(profile['age'], bins=bins, labels=labels, right=False)
profile.head()

# Wrangle the transcript data as required

# Get the transaction only 
sales_data = transcript[transcript["event"]=="transaction"].reset_index(drop=True)
sales_data.head()

# Retrieve the amount from the value column
sales_data["sales_amount"] = [ast.literal_eval(amount)["amount"] for amount in sales_data["value"]]
sales_data.drop("value", axis=1, inplace=True)
sales_data.head()

# Detect outliers
sns.boxplot(sales_data["sales_amount"])

# sales_data has many outliers. Lets filter the data to remain with sales 40

# remove outliers to find the real distributions of the sales amount 
sns.boxplot(sales_data[sales_data["sales_amount"]<40]["sales_amount"])


# Filter the data to remove outliers 
sales_data = sales_data[sales_data["sales_amount"]<40]

# Retrieve the rewards from the transcript data 
reward_data = transcript[transcript["event"]=='offer completed']
reward_data["reward"] = [ast.literal_eval(amount)["reward"] for amount in reward_data["value"]]
reward_data.drop("value", axis=1, inplace=True)
reward_data.reset_index(drop=True, inplace=True)


sales = list(sales_data["sales_amount"])
rewards = list(reward_data["reward"])

# fill the reward with null values 
null_list = np.full((len(sales)-len(rewards),), np.nan)

rewards.extend(null_list)

# Create a dataframe for two values reward and sales 
reward_sales = pd.DataFrame({
    "reward":rewards,
    "sales":sales
})


# **Set up the environment**

def environment():
    try:
        get_ipython()
        return "notebook"
    except:
        return "server"
environment()


# **Aesthetics for UI**

PALETTE = ["#ff6f69", "#ffcc5c", "#88d8b0", ]
pn.Row(
    pn.layout.HSpacer(height=50, background=PALETTE[0]),
    pn.layout.HSpacer(height=50, background=PALETTE[1]),
    pn.layout.HSpacer(height=50, background=PALETTE[2]),
)

# Make the dataframe interactive 
iportfolio = portfolio.interactive()

iprofile = profile.interactive()

ireward_sales = reward_sales.interactive()
ireward_sales.head()


# **Define panel widgets**

# X axis values 
xaxis = pn.widgets.RadioButtonGroup(
    name='X axis', 
    options=['reward', 'difficulty'],
    button_type='success'
)

# Y axis values 
yaxis = pn.widgets.RadioButtonGroup(
    name='Y axis', 
    options=['difficulty', 'duration'],
    button_type='success'
)

# demographics values 
demographics = pn.widgets.RadioButtonGroup(
    name='Demographics', 
    options=['gender', 'ageGroup'],
    button_type='success'
)


portfolio_pipeline = (iportfolio) # for portfolio

#for profile
profile_pipeline = (iprofile[[demographics, "income"]].groupby(demographics).mean().reset_index())

sales_pipeline = (ireward_sales) # for sales_rewards


if environment()=="server":
    theme="fast"
else:
    theme="simple"

# itable = ipipeline.pipe(pn.widgets.Tabulator, pagination='remote', page_size=10) #for portfolio

profile_table = profile_pipeline.pipe(pn.widgets.Tabulator, pagination='remote')
profile_table



# ihvplot = ipipeline.hvplot(x='mpg', y=yaxis, by='origin', color=PALETTE, line_width=6, height=400)
# ihvplot

ihvscatter = portfolio_pipeline.hvplot(x=xaxis, y=yaxis, by='offer_type', 
                              color=PALETTE, kind="scatter", height=500)



ihvbarchart = profile_pipeline.hvplot(x=demographics, y="income", 
                              color=PALETTE, kind="bar", width=600, height=500)

columns=['reward', 'sales']
density_plots = sales_pipeline.hvplot.kde(y=columns, alpha=0.5, 
                                          value_label='Distributions', legend='top_right',
                                         height=550)


template = pn.template.FastListTemplate(
    title='Starbuck Customer Segmentations Analysis', 
    sidebar=[pn.pane.Markdown("# Portfolio - Scatterplot"), 
             'X axis' , xaxis, 
             'Y axis' , yaxis, 
             pn.pane.Markdown("# Profile - Bar Chart"),
             'Demographics', demographics],
    main=[ihvscatter.panel(),
         (ihvbarchart+ profile_pipeline.hvplot.table(width=250)).panel(),
          density_plots.panel()
         ],
    accent_base_color="#88d8b0",
    header_background="#88d8b0",
)
# template.show()
template.servable();


# Please note that to get the Tabulator table styled nicely for dark mode you can set `theme='fast'` when you define the `itable`. It won't work in the notebook though.

# To *serve the dashboard* run `panel serve Dashboards.py`.
