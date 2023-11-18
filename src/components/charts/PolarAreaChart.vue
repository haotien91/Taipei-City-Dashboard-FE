
<script setup>
import { computed, defineProps, ref } from 'vue';
import { useMapStore } from '../../store/mapStore';

const props = defineProps(['chart_config', 'activeChart',"series", 'map_config']);
const mapStore = useMapStore();


const chartOptions = ref({
          chart: {
          type: 'PolarAreaChart',
        },
		yaxis:{
			labels: {
          offsetX: 200000,
      },
		},
		colors: props.chart_config.color,
		labels: props.chart_config.categories,
        stroke: {
              colors: ['#fff']
            },
            fill: {
              opacity: 0.8
            },
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 200
            },
			plotOptions: {
			polarArea: {
				rings: {
				strokeWidth: 1,
				strokeColor: '#e8e8e8',
				},
				spokes: {
				strokeWidth: 1,
				connectorColors: '#e8e8e8',
				}
			}
			},
		legend: {
			position: 'bottom', // 設置標籤位置為底部
		},
          }
        }]
});

const maxLabelLength = 1; // 你可以根据需要更改最大长度

// 计算属性，用于处理标签
const truncatedLabels = computed(() => {
  return props.chart_config.categories.map(label => {
    if (label.length > maxLabelLength) {
      // 如果标签长度超过最大长度，截取并添加省略号
      return label.slice(0, maxLabelLength) + '...';
    } else {
      return label;
    }
  });
});

// 更新 chartOptions 中的 labels 属性
chartOptions.value.labels = truncatedLabels.value;


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
	<div v-if="activeChart === 'PolarAreaChart'">
		<apexchart width="100%" height="500px" type="polarArea" :options="chartOptions" :series=[40610,15094,12234,108812,532547]
			@dataPointSelection="handleDataSelection"></apexchart>
	</div>
</template>