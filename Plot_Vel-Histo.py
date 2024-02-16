# 15/March/2023 update
# 09/March/2023
###########################################################################
## Histogram showing the velocity distribution of galaxy-members of A496 ##
###########################################################################



# libraries & dataset
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import pandas as pd
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
#sns.set(style="darkgrid")
sns.set(style="ticks")

fig, ax = plt.subplots(figsize=(10, 10))

# The diference with the version 200822 is that this new file (*_090323.csv) don't contain the HI galaxies that don't have optical velocity
df = pd.read_csv("files_tables/A496_table_all_memb_galaxies_090323.csv") 
#print(df)
HIall_data = pd.read_csv("files_tables/A496_table_all_HI_galaxies_200822.csv")


#Version plot2_Vel-Histo
HIall_non_det_data = pd.read_csv("files_tables/A496_table_all_HI_and_HI-non-det_galaxies_200822.csv") 
#print(HIall_non_det_data['HI_Nvspert'])
#print(HIall_non_det_data[63:])
#exit()


HI_Nvspert_colors= {'N':'#12a4e3','Habn':'#161616'}
HI_mass_colors= {'Massive':'#12a4e3','Poor':'yellow'}


#Version plot1_Vel-Histo
# HI-normal vs HI-abnormal.   In this figure we put the four types of HI-perturbed under the same symbol.  If you
# think is reasonable, we add the "incomplete" cases as part of the normal sample. 

#sns.histplot(data=df, x="Opt_vel", color="lightgreen", kde=True,binwidth=100, element="step", fill=True, hatch="//")
#sns.histplot(data=HIall_data, x="Mix_HI_Opt_vel", hue="HI_Nvspert",palette=HI_Nvspert_colors,binwidth=100, element="step", fill=True)

#Version plot2_Vel-Histo. Very similar to the previous one, but include the non-detections as part of the "abnormal ones". 
#Sale un error con la galaxia APMUKS(BJ) B042925.77-124531.4 por eso la quite

#sns.histplot(data=df, x="Opt_vel", color="lightgreen", kde=True,binwidth=100, element="step", fill=True, hatch="//")
#sns.histplot(data=HIall_non_det_data, x="Mix_HI_Opt_vel", hue="HI_Nvspert",palette=HI_Nvspert_colors,binwidth=100, element="step", fill=True)

#Version plot3_Vel-Histo. finally, let's plot the HI-rich dwarfs (m_stellar < E09 msolar) vs  the HI-normal massive ones (> E09 msolar).

sns.histplot(data=df, x="Opt_vel", color="lightgreen", kde=True,binwidth=100, element="step", fill=True, hatch="//")
sns.histplot(data=HIall_data, x="Mix_HI_Opt_vel", hue="Type_M_stellar",palette=HI_mass_colors,binwidth=100, element="step", fill=True)

plt.axvline(x=9884, ymax=0.2, color="red")# the velocity of the cluster
plt.text(9800,6.5,'v$_{cl}$', color='red', fontsize=12)

# add axis names        
plt.xlabel("v ($km/s$)")
plt.rcParams["legend.loc"] = 'upper right'
plt.ylabel("N")


red_line = mlines.Line2D([], [], color='red')
lightgreen_patch = mpatches.Patch(color='lightgreen',edgecolor='lightgreen',alpha=0.4,hatch="//")
lightblue_patch = mpatches.Patch(color='#12a4e3',edgecolor='#12a4e3',alpha=0.3)
grey_patch = mpatches.Patch(color='#161616',edgecolor='#161616',alpha=0.3)
yellow_patch = mpatches.Patch(color='yellow',edgecolor='yellow',alpha=0.3)


#Version plot1_Vel-Histo and plot2_Vel-Histo
#labels_Nvspert_colors= ['Member Galaxies','v$_{cl}$','HI normal','HI abnormal']
#handles_Nvspert=[lightgreen_patch,red_line, lightblue_patch,grey_patch]
#leg = ax.legend(handles_Nvspert,labels_Nvspert_colors,title='A496',loc='upper left',fontsize=12)

#Version plot3_Vel-Histo
labels_HImass_colors= ['Member Galaxies','v$_{cl}$','HI massive ','HI dwarfs']
handles_HI=[lightgreen_patch,red_line, lightblue_patch,yellow_patch]
leg = ax.legend(handles_HI,labels_HImass_colors,title='A496',loc='upper left',fontsize=12)


#plt.legend() 
plt.show()
