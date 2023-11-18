<!-- PolarAreaChart.vue -->
  <script setup>
  import { ref } from 'vue';
  
  const props = defineProps(['chart_config', 'activeChart', 'series']);
  const mapStore = useMapStore();
  const chartOptions = ref({
	chart: {
          type: 'Polar_Area',
        },
	colors: props.chart_config.color,
	dataLabels: {
	  enabled: false,
	},
	
	
	fill: {
          opacity: 0.8
        },
	stroke: {
          colors: ['#fff']
        },
	responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 200
            },
            legend: {
              position: 'bottom'
            }
          }
        }],
	
  });
  const chartHeight = computed(() => {
	return `${40 + props.series[0].data.length * 24}`;
});
const selectedIndex = ref(null);
function handleDataSelection(e, chartContext, config) {
	if (!props.chart_config.map_filter) {
		return;
	}
	if (config.dataPointIndex !== selectedIndex.value) {
		mapStore.addLayerFilter(`${props.map_config[0].index}-${props.map_config[0].type}`, props.chart_config.map_filter[0], props.chart_config.map_filter[1][config.dataPointIndex]);
		selectedIndex.value = config.dataPointIndex;
	} else {
		mapStore.clearLayerFilter(`${props.map_config[0].index}-${props.map_config[0].type}`);
		selectedIndex.value = null;
	}
}
  </script>
  <template>
	<div v-if="activeChart === 'Polar_Area'">
	  <apexchart width="100%" height="270px" type="Polar_Area" :options="chartOptions" :series="series"></apexchart>
	</div>
  </template>