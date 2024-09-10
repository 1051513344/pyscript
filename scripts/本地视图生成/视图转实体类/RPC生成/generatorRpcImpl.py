

if __name__ == "__main__":

    className = "Duty"

    rpcImplModel = """package com.bozhong.nursetransfer.interfaces;

import com.bozhong.nursetransfer.common.dto.resp.{className}RespDTO;
import com.bozhong.nursetransfer.core.Result;
import com.bozhong.nursetransfer.domain.{className}DO;
import com.bozhong.nursetransfer.mapper.hr.{className}DOMapper;
import com.bozhong.nursetransfer.service.{className}ReadServiceRPC;
import java.util.List;
import java.util.Map;
import cn.hutool.core.bean.BeanUtil;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import com.alibaba.dubbo.config.annotation.Service;

/**
 * @author 徐顺洁
 * @date 2024年08月15日 14:22:26
 */
@Service(interfaceClass = {className}ReadServiceRPC.class, version = "{dubboVersion}")
@Component
@Slf4j
public class {className}ReadServiceRPCImpl implements {className}ReadServiceRPC {open}

    @Autowired
    private {className}DOMapper {classLowerName}DOMapper;
    
    @Override
    public Result<List<{className}RespDTO>> listByWhere(Map<String, Object> params) {open}
        Result<List<{className}RespDTO>> result = new Result<>();
        List<{className}DO> list = {classLowerName}DOMapper.selectByWhere(params);
        result.setModule(BeanUtil.copyListProperties(list, {className}RespDTO.class));
        return result;
    {close}

{close}""".format(className=className, classLowerName=className[0].lower()+className[1:], open="{", close="}", dubboVersion="${dubbo.provider.version}")
    with open(f"{className}ReadServiceRPCImpl.java", "w", encoding='utf-8') as f:
        f.write(rpcImplModel)