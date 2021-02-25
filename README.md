<h1>Surfs-Up</h1>
<h2>Overview</h2>
<p>The purpose of this analysis is to determine whether year-round operation of a Surf and Ice Cream shop on the island of Oahu is a feasiable venture.  In order to complete the analysis termperature data was gathered from 9 weather stations for the months of June and December for the years 2010 through 2016 (December) and 2017 (June).</p>
<h2>Resources</h2>
<ul>
<li>Python v3.0</li>
<li>Data - hawaii.sqlite</li>
</ul>
<h2>Results</h2>
<p>Using the weather data described above the mean, variance, standard deviation, minimum, maximum, and percentiles of the temperature data for June and December were analyzed.  The results of which are shown and analyzed below.</p>
<ul>
<li>The 75% quartile for December is 74 degrees meaning that 75% of the temperatures are less than or equal to 74 degrees, whereas, the 25% quartile is 69 degrees meaning that only 25% of the temperatures are less than or equal to 69 degrees. This compares to June where the 75% quartile is 77 degrees and the 25% quartile is 73 degrees.
<li>The minimum temperature in June was 64 degrees, whereas, the minimum temperature in December was 56 degrees.</li>
<li>The maximum temperature in June was 85 degrees, whereas, the maximum temperature in December was 83 degrees.</li>
<li>The mean temperate in June was 75 degrees, whereas, the mean temperature in December was 71 degrees. However, the standard deviation is 3.25 for June and 3.75 for December both of which would be considered high.</li>
</ul>
<br>
<h3>June</h3>
<img src="https://github.com/bedwardssmith/surfs_up/blob/main/June_Statistics.png" alt="June Statistics">
<br>
  <h3>December</h3>
<img src="https://github.com/bedwardssmith/surfs_up/blob/main/December_Statistics.png" alt="Dec Statistics">
<br>
<h2>Summary</h2>
<p>The information provided by the statistical summaries would indicate that December would not necessarily be a booming month, however, in looking at the percentiles only 25% of the days are below 69 degrees therefore one would expect that December would not be a complete bust.  With a mean temperature of 71 degrees and a maximum temperature of 83 degrees there will likely be a sufficient number of days with warm temperatures to offset the cold days.</p>
<p>However, prior to making an assumption that the shop would be viable as a sustainable year-round venture I would conduct the following additional queries:</p>
<ul>
<li>As land topography can affect weather I would run queries on the individual stations to determine if there is an optimal location.</li>
<li>Although temperature is an important factor to year-round success it is not the only factor.  Precipitation amounts should be queried for each of the weather stations.  Although the temperature statistics for the month of December would indicate that year-round operation would be feasible the precipitation statistics may indicate otherwise.  That is with cooler December temperatures combined with significant amounts of precipitation year-round operation may not be feasible.</li>
<li>Given the high standard deviation for both June and December I would reduce the number of years included in the dataset to see if this reduces the standard deviation; use data for the years 2014 through 2017.</li>
</ul>
